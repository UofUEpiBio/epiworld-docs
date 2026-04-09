# SIS Model

*Source:
[`examples/01-sis`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/01-sis)*

This example runs the built-in `ModelSIS` for 100 days. Because there is no
permanent immunity in SIS, the system reaches an **endemic equilibrium** where
a proportion of the population remains infected indefinitely.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

int main() {

    epimodels::ModelSIS<> model(
        "a virus", // Name of the virus
        0.01,      // Initial prevalence
        0.9,       // Infectiousness
        0.5        // Recovery rate
    );

    // Adding a small-world graph
    model.agents_from_adjlist(
        rgraph_smallworld(10000, 5, .001, false, model)
    );

    // Running and checking the results
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

Name of the model   : Susceptible-Infected-Susceptible (SIS)
Population size     : 10000
Agents' data        : (none)
Number of entities  : 0
Days (duration)     : 100 (of 100)
Number of viruses   : 1
Last run elapsed t  : 64.00ms
Last run speed      : 15.51 million agents x day / second
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

Distribution of the population at time 100:
  - (0) Susceptible :  9900 -> 3515
  - (1) Infected    :   100 -> 6485

Transition Probabilities:
 - Susceptible  0.53  0.47
 - Infected     0.50  0.50
```
