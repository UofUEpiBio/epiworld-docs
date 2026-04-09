# Generation Interval

*Source:
[`examples/13-genint`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/13-genint)*

This example computes and compares **expected** vs. **observed** generation
intervals for both SIR and SEIR connected-population models.

## Source Code

```cpp
#include <iostream>
#include <vector>
#include <math.h>
#include <random>
#include "epiworld.hpp"

using namespace epiworld;

int main()
{
    double r          = 10.0;       // Contact rate
    double popsize    = 1e5;
    double p_i        = .1;         // Probability of infection
    double p_r        = 1.0/7.0;    // Probability of recovery
    double incubation = 2.0;        // Incubation period
    size_t nsteps     = 200;
    size_t max_days_for_calc = 20;

    // --- SIR Connected ---
    epimodels::ModelSIRCONN<> model(
        "avirus", popsize, 50.0/popsize, r, p_i, p_r
    );

    model.run(nsteps, 554);
    model.print();

    std::vector<int> agent, virus, time, gentime_sir_obs;
    model.get_db().get_generation_time(
        agent, virus, time, gentime_sir_obs);

    auto gentime_sir = model.generation_time_expected();
    double gentime_sir_mean = std::accumulate(
        gentime_sir.begin(),
        gentime_sir.begin() + max_days_for_calc, 0.0
    ) / max_days_for_calc;

    // Observed mean (conditioning on gentime >= 0)
    double gentime_sir_obs_mean = 0.0;
    size_t n = 0;
    for (int i = 0; i < static_cast<int>(gentime_sir_obs.size()*3/4); i++) {
        if (time[i] >= static_cast<int>(max_days_for_calc))
            continue;
        if (gentime_sir_obs[i] >= 0) {
            gentime_sir_obs_mean += gentime_sir_obs[i];
            n++;
        }
    }
    gentime_sir_obs_mean /= n;

    // --- SEIR Connected ---
    epimodels::ModelSEIRCONN<> model2(
        "avirus", popsize, 50.0/popsize, r, p_i, incubation, p_r
    );

    model2.run(nsteps, 554);
    model2.print();

    std::vector<int> agent2, virus2, time2, gentime_seir_obs;
    model2.get_db().get_generation_time(
        agent2, virus2, time2, gentime_seir_obs);

    auto gentime_seirconn = model2.generation_time_expected();
    double gentime_seirconn_mean = std::accumulate(
        gentime_seirconn.begin(),
        gentime_seirconn.begin() + max_days_for_calc, 0.0
    ) / max_days_for_calc;

    double gentime_seir_obs_mean = 0.0;
    n = 0;
    for (int i = 0; i < static_cast<int>(gentime_seir_obs.size()*3/4); i++) {
        if (time[i] >= static_cast<int>(max_days_for_calc))
            continue;
        if (gentime_seir_obs[i] >= 0) {
            gentime_seir_obs_mean += gentime_seir_obs[i];
            n++;
        }
    }
    gentime_seir_obs_mean /= n;

    std::cout << "SIR Gen. Int. (obs)       : "
              << gentime_sir_obs_mean << std::endl;
    std::cout << "SIR Gen. Int. (expected)  : "
              << gentime_sir_mean << std::endl;
    std::cout << "SEIR Gen. Int. (obs)      : "
              << gentime_seir_obs_mean << std::endl;
    std::cout << "SEIR Gen. Int. (expected) : "
              << gentime_seirconn_mean << std::endl;

    return 0;
}
```

## Key Takeaways

- `get_db().get_generation_time()` retrieves observed generation intervals from
  the simulation database.
- `generation_time_expected()` computes the analytically expected generation
  interval based on model parameters.
- Comparing the two helps validate model behavior and understand how incubation
  (in SEIR) lengthens the generation interval relative to SIR.
