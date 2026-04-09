# SIR Model

*Source:
[`examples/01-sir`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/01-sir)*

This example runs the built-in `ModelSIR` on a small-world network with
50,000 agents for 50 days.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

int main() {

    epimodels::ModelSIR<> model(
        "a virus", // Name of the virus
        0.01,      // Initial prevalence
        0.9,       // Infectiousness
        0.5        // Recovery rate
    );

    // Adding a small-world graph
    model.agents_from_adjlist(
        rgraph_smallworld(50000, 20, .01, false, model)
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

Name of the model   : Susceptible-Infected-Recovered (SIR)
Population size     : 50000
Agents' data        : (none)
Number of entities  : 0
Days (duration)     : 50 (of 50)
Number of viruses   : 1
Last run elapsed t  : 35.00ms
Last run speed      : 70.16 million agents x day / second
Rewiring            : off

Global events:
 (none)

Virus(es):
 - a virus

Tool(s):
 (none)

Model parameters:
 - Recovery rate     : 0.5000
 - Transmission rate : 0.9000

Distribution of the population at time 50:
  - (0) Susceptible : 49500 -> 0
  - (1) Infected    :   500 -> 0
  - (2) Recovered   :     0 -> 50000

Transition Probabilities:
 - Susceptible  0.75  0.25     -
 - Infected        -  0.50  0.50
 - Recovered       -     -  1.00
```
