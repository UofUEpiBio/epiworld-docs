# Advanced Usage

*Source:
[`examples/04-advanced-usage`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/04-advanced-usage)*

This example demonstrates several advanced features in a single model:

- **Sequence-based viruses** with a binary sequence that can mutate.
- **Custom mutation function** using `EPI_NEW_MUTFUN`.
- **Post-recovery immunity** that grants a tool after clearing the virus.
- **Multiple tools**: immune system, vaccine, face masks, and post-immunity.
- **Network rewiring** using degree-sequence preserving randomization.

## Source Code

```cpp
#include "epiworld.hpp"

// Original data will be an integer vector
#define DAT std::vector<int>
static DAT base_seq = {
    true, false, false, true, true,
    false, true, false, true, false, false
};

// Defining mutation function
EPI_NEW_MUTFUN(covid19_mut, DAT) {
    if (EPI_RUNIF() < m->par("Mutation rate")) {
        int idx = std::floor(EPI_RUNIF() * v.get_sequence()->size());
        DAT tmp_seq = *v.get_sequence();
        tmp_seq[idx] = !v.get_sequence()->at(idx);
        v.set_sequence(tmp_seq);
        return true;
    }
    return false;
}

// Post covid recovery — grant immunity tool
EPI_NEW_POSTRECOVERYFUN(post_covid, DAT) {
    auto Tptr = m->get_tools()[3u];
    Tptr->set_sequence(*v.get_sequence());
    p->add_tool(Tptr);
}

int main() {
    epiworld::Model<DAT> model;

    model.add_state("Susceptible", epiworld::default_update_susceptible<DAT>);
    auto exposed_state =
        model.add_state("Exposed", epiworld::default_update_exposed<DAT>);
    auto recovered_state = model.add_state("Recovered");
    auto removed_state   = model.add_state("Removed");

    model.agents_from_adjlist(
        "edgelist.txt", 1000, 0, false
    );

    // Model parameters
    model.add_param(0.001, "Mutation rate");
    model.add_param(0.90, "vax efficacy");
    model.add_param(0.0001, "vax death");
    model.add_param(0.10, "imm efficacy");
    model.add_param(0.10, "imm recovery");
    model.add_param(0.001, "imm death");
    model.add_param(0.90, "imm trans");
    model.add_param(0.01, "virus death");

    // Virus
    epiworld::Virus<DAT> covid19("COVID19", 0.01, true);
    covid19.set_sequence(base_seq);
    covid19.set_mutation(covid19_mut);
    covid19.set_post_recovery(post_covid);
    covid19.set_prob_death("virus death");
    covid19.set_state(exposed_state, recovered_state, removed_state);

    // Tools
    epiworld::Tool<DAT> immune("Immune system", 1.0, true);
    immune.set_susceptibility_reduction("imm efficacy");
    immune.set_recovery_enhancer("imm recovery");
    immune.set_death_reduction("imm death");
    immune.set_transmission_reduction("imm trans");
    DAT seq0(base_seq.size(), false);
    immune.set_sequence(seq0);

    epiworld::Tool<DAT> vaccine("Vaccine", 0.5, true);
    vaccine.set_susceptibility_reduction("vax efficacy");
    vaccine.set_recovery_enhancer(0.4);
    vaccine.set_death_reduction("vax death");
    vaccine.set_transmission_reduction(0.5);

    epiworld::Tool<DAT> mask("Face masks", 0.5, true);
    mask.set_susceptibility_reduction(0.8);
    mask.set_transmission_reduction(0.05);

    epiworld::Tool<DAT> post_immunity("Post Immune", 0, true);
    post_immunity.set_susceptibility_reduction(1.0);

    model.add_virus(covid19);
    model.add_tool(immune);
    model.add_tool(vaccine);
    model.add_tool(mask);
    model.add_tool(post_immunity);

    // Rewiring
    model.queuing_off();
    model.set_rewire_fun(
        [](std::vector<epiworld::Agent<DAT>>* agents,
           epiworld::Model<DAT>* m, float p) {
            epiworld::rewire_degseq<DAT>(
                reinterpret_cast<epiworld::AdjList*>(agents), m, p);
        }
    );
    model.set_rewire_prop(0.10);

    model.print();
    model.run(60, 123);
    model.print();

    return 0;
}
```

## Key Takeaways

- **Mutation**: The `EPI_NEW_MUTFUN` macro defines a function that flips a
  random bit in the virus sequence with probability equal to the
  "Mutation rate" parameter.
- **Post-recovery**: `EPI_NEW_POSTRECOVERYFUN` grants the agent a
  "Post Immune" tool whose sequence matches the virus they recovered from.
- **Rewiring**: `set_rewire_fun()` with `rewire_degseq` randomizes edges while
  preserving the degree sequence, modeling changing social contacts.
