# Concepts

This section covers the core theoretical concepts and mechanisms behind
epiworld simulations. Understanding these concepts is essential for
building and customizing epidemiological models.

## Overview

Epiworld is a general-purpose agent-based modeling (ABM) framework for
epidemiological simulation. Unlike many frameworks that come with a fixed set of
compartments (e.g., SIR only), epiworld lets you define an **arbitrary set of
states** and their update rules. This flexibility, combined with high
performance, makes it suitable for both rapid prototyping and large-scale
simulations.

## Key Topics

- [**Simulation Steps**](simulation-steps.md) — How a single day of the
  simulation is executed, including agent updates, global events, network
  rewiring, and state recording.

- [**Agents**](agents.md) — The individual units of the simulation. Agents
  carry viruses and tools, interact through a contact network, and transition
  between states.

- [**Contagion**](contagion.md) — The mathematical model governing how
  susceptible agents acquire viruses from their infected contacts, including
  multi-virus competition.
