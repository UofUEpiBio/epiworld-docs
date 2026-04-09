# Hello World

*Source:
[`examples/00-hello-world`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/00-hello-world)*

This example builds a model from scratch using `add_state()` instead of relying
on a built-in model class. It defines four states (Susceptible, Exposed,
Recovered, Removed), adds a virus and a vaccine tool, generates a small-world
network, and runs the simulation for 100 days.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

int main()
{
    // Creating a model
    epiworld::Model<int> model;

    // Declaring the three states in the model
    model.add_state("Susceptible", epiworld::default_update_susceptible<int>);
    auto exposed_state = model.add_state(
        "Exposed", epiworld::default_update_exposed<int>);
    auto recovered_state = model.add_state("Recovered");
    auto removed_state = model.add_state("Removed");

    // Adding the tool and virus
    epiworld::Virus<int> virus("covid 19");
    virus.set_distribution(
        distribute_virus_randomly<int>(50, false));

    virus.set_post_immunity(1.0);
    virus.set_state(exposed_state, recovered_state, removed_state);
    virus.set_prob_death(.01);
    model.add_virus(virus);

    epiworld::Tool<int> tool("vaccine", .5, true);
    model.add_tool(tool);

    // Generating a random pop
    model.agents_smallworld(10000, 20, false, .01);

    // Running the model
    model.run(100, 123);
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
Population size     : 10000
Agents' data        : (none)
Number of entities  : 0
Days (duration)     : 100 (of 100)
Number of viruses   : 1
Last run elapsed t  : 16.00ms
Last run speed      : 60.72 million agents x day / second
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
  - (0) Susceptible :  9950 -> 0
  - (1) Exposed     :    50 -> 0
  - (2) Recovered   :     0 -> 9423
  - (3) Removed     :     0 -> 577

Transition Probabilities:
 - Susceptible  0.78  0.22     -     -
 - Exposed         -  0.85  0.14  0.01
 - Recovered       -     -  1.00     -
 - Removed         -     -     -  1.00
```
