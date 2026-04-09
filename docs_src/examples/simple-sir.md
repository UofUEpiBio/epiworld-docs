# Simple SIR

*Source:
[`examples/03-simple-sir`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/03-simple-sir)*

This example builds a SIR model from scratch (without `ModelSIR`) using
`add_state()` and the library's default update functions. It adds a vaccine
tool and runs on a 1,000-agent small-world network.

## Source Code

```cpp
#include "epiworld.hpp"

int main()
{
    // Creating a model
    epiworld::Model<> model;

    model.add_state("Susceptible", epiworld::default_update_susceptible<>);
    auto infected_state = model.add_state(
        "Infected", epiworld::default_update_exposed<>);
    auto removed_state = model.add_state("Removed");

    // Creating a virus
    epiworld::Virus<> covid19("covid 19", 0.05, true);
    covid19.set_prob_infecting(0.8);
    covid19.set_state(infected_state, removed_state, removed_state);

    // Creating a tool
    epiworld::Tool<> vax("vaccine", .5, true);
    vax.set_susceptibility_reduction(.95);

    // Adding the tool and virus
    model.add_virus(covid19);
    model.add_tool(vax);

    // Generating a random pop
    model.agents_from_adjlist(
        epiworld::rgraph_smallworld(1000, 5, 0.01, false, model)
    );

    // Running the model
    model.run(100, 123123);
    model.print();

    return 0;
}
```

## Output

```
_________________________________________________________________________
Running the model...
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| done.
________________________________________________________________________________
________________________________________________________________________________
SIMULATION STUDY

Name of the model   : (none)
Population size     : 1000
Agents' data        : (none)
Number of entities  : 0
Days (duration)     : 100 (of 100)
Number of viruses   : 1
Last run elapsed t  : 6.00ms
Last run speed      : 15.99 million agents x day / second
Rewiring            : off

Global events:
 (none)

Virus(es):
 - covid 19

Tool(s):
 - vaccine

Model parameters:
 (none)

Distribution of the population at time 100:
  - (0) Susceptible :  950 -> 588
  - (1) Infected    :   50 -> 0
  - (2) Removed     :    0 -> 412

Transition Probabilities:
 - Susceptible  0.99  0.01     -
 - Infected        -  0.85  0.15
 - Removed         -     -  1.00
```
