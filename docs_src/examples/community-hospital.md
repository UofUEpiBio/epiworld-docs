# Community–Hospital Model

*Source:
[`examples/14-community-hosp`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/14-community-hosp)*

This example builds a **two-population model** where individuals can move
between a community setting and a hospital. It demonstrates how to subclass
`Model` and define custom update functions for each state.

## Overview

- **Susceptible** agents live in the community and can become infected.
- **Infected** agents in the community may recover, or be hospitalized.
- **Infected (hospitalized)** agents may recover and be discharged, or remain
  hospitalized, or be discharged while still infected.

Transmission only occurs within the community — hospitalized patients are
isolated from the community contact network.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

class CommunityHospModel : public Model<int> {
public:
    unsigned long long susceptible_state;
    unsigned long long infected_state;
    unsigned long long infected_hospitalized_state;
    CommunityHospModel();
};

// Sampler that excludes hospitalized from community transmission
auto get_sampler_suscept = [](CommunityHospModel* m) {
    return sampler::make_sample_virus_neighbors<>(
        {m->infected_hospitalized_state});
};

inline void update_susceptible(Agent<int>* p, Model<int>* m) {
    auto hm = static_cast<CommunityHospModel*>(m);
    auto virus = get_sampler_suscept(hm)(p, m);
    if (virus != nullptr) {
        if (m->par("Prob hospitalization") > m->runif())
            p->set_virus(*m, *virus, hm->infected_hospitalized_state);
        else
            p->set_virus(*m, *virus, hm->infected_state);
    }
}

inline void update_infected(Agent<int>* p, Model<int>* m) {
    auto hm = static_cast<CommunityHospModel*>(m);
    std::vector<epiworld_double> probs = {
        m->par("Prob hospitalization"),
        m->par("Prob recovery")
    };
    int res = roulette<>(probs, m);
    if (res == 0)
        p->change_state(*m, hm->infected_hospitalized_state);
    else if (res == 1)
        p->rm_virus(*m, hm->susceptible_state);
}

inline void update_infected_hospitalized(
    Agent<int>* p, Model<int>* m
) {
    auto hm = static_cast<CommunityHospModel*>(m);
    if (m->par("Prob recovery") > m->runif())
        p->rm_virus(*m, hm->susceptible_state);
    else if (m->par("Discharge infected") > m->runif())
        p->change_state(*m, hm->infected_state);
}

CommunityHospModel::CommunityHospModel() : Model<int>() {
    susceptible_state = add_state("Susceptible", update_susceptible);
    infected_state = add_state("Infected", update_infected);
    infected_hospitalized_state = add_state(
        "Infected (hospitalized)", update_infected_hospitalized);
}

int main() {
    auto model = CommunityHospModel();

    Virus<> mrsa("MRSA");
    mrsa.set_state(
        model.infected_state,
        model.susceptible_state,
        model.susceptible_state);
    mrsa.set_prob_infecting(.1);
    mrsa.set_prob_recovery(.33);
    mrsa.set_distribution(distribute_virus_randomly<>(0.01));
    model.add_virus(mrsa);

    model.agents_smallworld(1000, 4, false, 0.1);
    model.add_param(0.1, "Prob hospitalization");
    model.add_param(0.33, "Prob recovery");
    model.add_param(0.1, "Discharge infected");

    model.run(100, 1231);
    model.print();

    return 0;
}
```

## Key Takeaways

- **Subclassing `Model`** lets you store state IDs as member variables for
  convenient access across update functions.
- **`sampler::make_sample_virus_neighbors`** can exclude specific states from
  the neighbor sampling, effectively modeling isolation.
- **`roulette()`** performs a weighted random draw, useful when an agent can
  transition to multiple states with different probabilities.
