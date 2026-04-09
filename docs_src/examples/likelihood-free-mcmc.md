# Likelihood-Free MCMC

*Source:
[`examples/10-likelihood-free-mcmc`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/10-likelihood-free-mcmc)*

This example demonstrates how to use epiworld's built-in **LFMCMC**
(Likelihood-Free Markov Chain Monte Carlo) module to estimate parameters of an
SIR model. The approach generates simulated data at each MCMC step and compares
it to observed data using a kernel function — no explicit likelihood is needed.

## Source Code

```cpp
#include "epiworld.hpp"
#include "epiworld/math/lfmcmc.hpp"

using namespace epiworld;

epimodels::ModelSIR<> model(
    "covid", .1, .1, .3
);

std::vector< int > simfun(
    std::vector< epiworld_double > params,
    LFMCMC<std::vector<int>> *
) {
    model.set_param("Recovery rate", params[0u]);
    model.set_param("Transmission rate", params[1u]);
    model.reset();
    model.run(50);

    std::vector< int > res;
    model.get_db().get_today_total(nullptr, &res);
    return res;
}

void sumfun(
    std::vector< epiworld_double > & res,
    const std::vector< int > & dat,
    LFMCMC< std::vector<int> > *
) {
    if (res.size() == 0u)
        res.resize(dat.size());
    for (size_t i = 0u; i < dat.size(); ++i)
        res[i] = static_cast< epiworld_double >(dat[i]);
}

int main()
{
    model.agents_smallworld(1000);

    LFMCMC<std::vector< int >> lfmcmc;
    lfmcmc.set_simulation_fun(simfun);
    lfmcmc.set_summary_fun(sumfun);
    lfmcmc.set_proposal_fun(
        make_proposal_norm_reflective<std::vector<int>>(.5, 0, 1));
    lfmcmc.set_kernel_fun(kernel_fun_gaussian<std::vector<int>>);

    // Generate observed data
    model.verbose_off();
    model.run(50, 122);
    model.print();

    std::vector< int > obs_dat;
    model.get_db().get_today_total(nullptr, &obs_dat);

    lfmcmc.set_observed_data(obs_dat);
    lfmcmc.set_rand_engine(model.get_rand_endgine());

    std::vector< epiworld_double > par0 = {.5, .5};
    lfmcmc.run(par0, 2000, 1);

    lfmcmc.set_params_names({"Immune recovery", "Infectiousness"});
    lfmcmc.set_stats_names(model.get_states());
    lfmcmc.print();
}
```

## Key Takeaways

- The `LFMCMC` class orchestrates parameter estimation without a closed-form
  likelihood.
- `simfun` re-runs the SIR model at each MCMC step with proposed parameters.
- `sumfun` converts simulation output into summary statistics for comparison.
- A reflective normal proposal keeps parameters within `[0, 1]`.
