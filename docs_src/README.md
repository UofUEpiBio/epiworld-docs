# Epiworld Documentation

A fast, general-purpose C++ framework for agent-based epidemiological simulation.

---

## What is Epiworld?

Epiworld is a high-performance C++ library for building and running
epidemiological simulations. It is designed for **rapid prototyping** of
complex models while maintaining the speed needed for large-scale studies.

**Key features:**

- :material-lightning-bolt: **Fast** — Over 150 million agent × day simulations per second.
- :material-puzzle: **Flexible** — Define arbitrary states, viruses, tools, and update rules.
- :material-file-code: **Header-only** — Single-file include; depends only on the C++ standard library.
- :material-lan: **Network-aware** — Simulations run on contact networks with configurable topologies.
- :material-bacteria: **Multi-pathogen** — Multiple viruses and tools can coexist in one simulation.

## Quick Example

```cpp
#include "epiworld.hpp"

using namespace epiworld;

int main() {

    // Create a built-in SIR model
    epimodels::ModelSIR<> model(
        "COVID-19", // Virus name
        0.01,       // Initial prevalence
        0.1,        // Transmission rate
        0.3         // Recovery rate
    );

    // Generate a small-world contact network
    model.agents_smallworld(100000, 10, false, 0.01);

    // Run for 100 days with seed 122
    model.run(100, 122);
    model.print();

    return 0;
}
```

## Documentation Sections

<div class="grid cards" markdown>

-   :material-lightbulb:{ .lg .middle } **Concepts**

    ---

    Core theory behind epiworld: simulation steps, agents, and contagion
    mechanics.

    [:octicons-arrow-right-24: Read more](concepts/index.md)

-   :material-virus:{ .lg .middle } **Models**

    ---

    Pre-built epidemiological models (SIR, SEIR, measles, etc.) ready to use
    or customize.

    [:octicons-arrow-right-24: Browse models](models/index.md)

-   :material-cog:{ .lg .middle } **Implementation**

    ---

    Architecture, performance optimization, extending the library, and
    internal design details.

    [:octicons-arrow-right-24: Learn more](impl/index.md)

-   :material-code-tags:{ .lg .middle } **API Reference**

    ---

    Complete class and function reference generated from the source code.

    [:octicons-arrow-right-24: API docs](api/index.md)

</div>

## Source Code

The epiworld source code is hosted at
[**UofUEpiBio/epiworld**](https://github.com/UofUEpiBio/epiworld) on GitHub.
This documentation site is built from the
[**UofUEpiBio/epiworld-docs**](https://github.com/UofUEpiBio/epiworld-docs)
repository and always reflects the latest version of the library.
