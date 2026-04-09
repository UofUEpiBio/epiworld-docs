# SEIR Model

*Source:
[`examples/01-seir`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/01-seir)*

This example runs the built-in `ModelSEIR` on a small-world network with
1,000,000 agents for 50 days, demonstrating epiworld's performance at scale.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

int main() {

    epimodels::ModelSEIR<> model(
        "a virus", // Name of the virus
        0.01,      // Initial prevalence
        0.9,       // Infectiousness
        7,         // Incubation days
        0.5        // Recovery rate
    );

    // Adding a small-world graph
    model.agents_from_adjlist(
        rgraph_smallworld(1000000, 5, .001, false, model)
    );

    // Running and checking the results
    model.run(50, 123);
    model.print();

    return 0;
}
```

## Output

```
_________________________________________________________________________
|Running the model...
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| done.
|________________________________________________________________________________
________________________________________________________________________________
SIMULATION STUDY

Name of the model   : Susceptible-Exposed-Infected-Removed (SEIR)
Population size     : 1000000
Agents' data        : (none)
Number of entities  : 0
Days (duration)     : 50 (of 50)
Number of viruses   : 1
Last run elapsed t  : 825.00ms
Last run speed      : 60.59 million agents x day / second
Rewiring            : off

Global events:
 (none)

Virus(es):
 - a virus

Tool(s):
 (none)

Model parameters:
 - Incubation days   : 7.0000
 - Recovery rate     : 0.5000
 - Transmission rate : 0.9000

Distribution of the population at time 50:
  - (0) Susceptible :  990000 -> 118466
  - (1) Exposed     :   10000 -> 51970
  - (2) Infected    :       0 -> 16394
  - (3) Removed     :       0 -> 813170

Transition Probabilities:
 - Susceptible  0.96  0.04     -     -
 - Exposed         -  0.86  0.14     -
 - Infected        -     -  0.50  0.50
 - Removed         -     -     -  1.00
```
