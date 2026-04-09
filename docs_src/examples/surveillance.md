# Surveillance Model

*Source:
[`examples/07-surveillance`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/07-surveillance)*

This example runs the built-in `ModelSURV` (Surveillance) model, which
integrates vaccination, latency, symptomatic vs. asymptomatic infection,
detection, and mortality into a single framework.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

int main(int argc, char* argv[]) {

    epiworld_fast_uint ndays   = 100;
    epiworld_fast_uint popsize = 10000;
    epiworld_fast_uint preval  = 10;
    epiworld_double sur_prob   = 0.001;

    epimodels::ModelSURV<> model(
        "a virus",   // Name of the virus
        preval,      // prevalence
        0.9,         // efficacy_vax
        3u,          // latent_period
        12u,         // infect_period
        .7,          // prob_symptoms
        .25,         // prop_vaccinated
        .5,          // prop_vax_redux_transm
        .5,          // prop_vax_redux_infect
        sur_prob,    // surveillance_prob
        1.0,         // prob_transmission
        0.001,       // Prob death
        0.1          // Prob re-infect
    );

    // Adding a small-world graph
    model.agents_from_adjlist(
        epiworld::rgraph_smallworld(popsize, 5, .01, false, model)
    );

    // Running and checking the results
    model.run(ndays, 123);
    model.print();

    return 0;
}
```

## Key Takeaways

- `ModelSURV` combines vaccination, infection, detection, and death in a
  surveillance-oriented framework.
- It tracks detected vs. undetected infections and includes reinfection
  probability.
- The model also collects user data internally for surveillance analysis.
