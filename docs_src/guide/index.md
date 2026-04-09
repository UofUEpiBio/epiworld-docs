# User Guide

This guide introduces the core concepts of epiworld and walks you through
building and running epidemiological simulations. Each chapter builds on the
previous one, so we recommend reading them in order if you are new to the
library.

## Getting Started

<div class="grid cards" markdown>

-   :material-lightbulb:{ .lg .middle } **Introduction**

    ---

    What epiworld is, how simulations work, and the key abstractions
    (agents, viruses, tools, states).

    [:octicons-arrow-right-24: Fundamentals](fundamentals.md)

-   :material-hammer-wrench:{ .lg .middle } **Building Models**

    ---

    How to create a model from scratch using `add_state()`, define custom
    update functions, and wire up a contact network.

    [:octicons-arrow-right-24: Building Models](building-models.md)

-   :material-virus:{ .lg .middle } **Viruses, Tools & Events**

    ---

    Adding viruses and tools to a simulation, configuring global events,
    and collecting custom data.

    [:octicons-arrow-right-24: Viruses, Tools & Events](viruses-tools-events.md)

</div>

## Core Concepts

These pages describe the mechanics that drive every epiworld simulation:

- [**Simulation Steps**](../concepts/simulation-steps.md) — How a single day is
  executed: agent updates, global events, network rewiring, and recording.
- [**Agents**](../concepts/agents.md) — The individual units that carry viruses
  and tools, interact through a contact network, and transition between states.
- [**Contagion**](../concepts/contagion.md) — The mathematical model governing
  disease transmission, including multi-virus competition.

## Built-in Models

Epiworld ships with a collection of ready-to-use epidemiological models.
See the [Built-in Models](../models/index.md) section for a full catalog with
usage examples.

## Advanced Topics

For deeper dives into the library internals, performance tuning, and extension
points, see the [Advanced Topics](../advanced/index.md) section.
