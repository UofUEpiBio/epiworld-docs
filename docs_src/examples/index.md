# Examples

This section showcases runnable examples from the
[epiworld repository](https://github.com/UofUEpiBio/epiworld/tree/master/examples).
Each example includes the full C++ source code and the corresponding output.

To build and run any example locally, clone the epiworld repository and use
`make`:

```bash
git clone https://github.com/UofUEpiBio/epiworld.git
cd epiworld
make build/examples/<example-name>/<example-name>
./build/examples/<example-name>/<example-name>
```

## Example Index

| Example | Description |
|---------|-------------|
| [Hello World](hello-world.md) | Build a custom SEIR model from scratch using `add_state()` |
| [SIR](sir.md) | Run a built-in SIR model on a small-world network |
| [SEIR](seir.md) | Run a built-in SEIR model with 1 million agents |
| [SIS](sis.md) | Run a built-in SIS model showing endemic equilibrium |
| [Multiple Runs](multiple-runs.md) | Run 100 replicates of an SIR model and collect results |
| [Simple SIR](simple-sir.md) | A hand-built SIR using `add_state()` with a vaccine tool |
| [Advanced Usage](advanced-usage.md) | Mutation, rewiring, and multiple tools in a single model |
| [User Data](user-data.md) | Custom data collection with `set_user_data()` and post-recovery hooks |
| [Surveillance](surveillance.md) | The SURV model with vaccination, detection, and reporting |
| [Likelihood-Free MCMC](likelihood-free-mcmc.md) | Parameter estimation using LFMCMC |
| [Entities](entities.md) | Population mixing with SEIR and contact matrices |
| [Generation Interval](generation-interval.md) | Computing expected vs. observed generation intervals |
| [Community–Hospital](community-hospital.md) | A two-population model with admission and discharge dynamics |
