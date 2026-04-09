# Multiple Runs

*Source:
[`examples/02-sir_multiple_runs`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/02-sir_multiple_runs)*

This example demonstrates how to run multiple replicates of an SIR model,
collect the final state counts from each run, and print summary statistics.
It uses `set_backup()` and `reset()` to efficiently re-run the same model
configuration.

## Source Code

```cpp
#include "epiworld.hpp"
#include <iostream>

using namespace epiworld;

int main() {

    int total_replicates = 100;

    epimodels::ModelSIR<> sir(
        "a virus", // Name of the virus
        0.01,      // Initial prevalence
        0.9,       // Infectiousness
        0.3        // Recovery rate
    );

    // Adding a small-world graph
    sir.agents_from_adjlist(
        rgraph_smallworld(1000, 5, .01, false, sir)
    );

    // Running and checking the results
    std::vector< std::vector< int > > results(total_replicates);
    std::vector< std::string > labels;
    sir.set_backup();
    sir.verbose_off();

    sir.seed(123);
    for (int r = 0; r < total_replicates; ++r)
    {
        sir.run(60);
        sir.get_db().get_today_total(&labels, &results[r]);
        sir.reset();
        std::cout << "Replicate " << r << " done" << std::endl;
    }

    sir.get_elapsed();

    for (epiworld_fast_uint s = 0u; s < labels.size(); ++s)
        printf("%s, ", labels[s].c_str());
    printf("\n");

    for (epiworld_fast_uint r = 0u; r < 10; ++r)
    {
        for (epiworld_fast_uint s = 0u; s < labels.size(); ++s)
            printf("%i, ", results[r][s]);
        printf("\n");
    }

    return 0;
}
```

## Output (first 10 replicates)

```
Replicate 0 done
Replicate 1 done
...
Replicate 99 done
last run elapsed time : 0.00ms
total elapsed time    : 27.00ms
total runs            : 100
mean run elapsed time : 0.27ms
Susceptible, Infected, Recovered,
2, 5, 993,
0, 0, 1000,
0, 0, 1000,
0, 0, 1000,
0, 6, 994,
0, 0, 1000,
0, 0, 1000,
3, 10, 987,
0, 8, 992,
0, 1, 999,
```
