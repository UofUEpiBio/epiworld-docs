# Contagion

Susceptible individuals can acquire a virus from any of their infected
connections. This page describes the mathematical model governing disease
transmission in epiworld.

## Transmission Probability

The probability that susceptible individual $i$ gets virus $v$ from
individual $j$ depends on three factors:

1. **Transmissibility of the virus**, $P_v \in [0,1]$
2. **Contagion reduction factor** of individual $i$, $C_r \in [0,1]$
3. **Transmission reduction factor** of the host $j$, $T_r \in [0,1]$

The last two factors are computed from $i$ and $j$'s **tools** (e.g.,
vaccines, masks). The resulting probability of $i$ getting virus $v$
from $j$ is:

$$
P(\text{Virus } v) = P_v \times (1 - C_r) \times (1 - T_r)
$$

## Single-Virus Constraint

By default, epiworld assumes that individuals can acquire **at most one
virus** at a time. Under this constraint, the actual probability that agent
$i$ acquires virus $v$ from agent $j$ is:

$$
P_{ivj} = P(\text{Virus } v \mid \text{at most one virus})
$$

This is calculated using **Bayes' rule**:

$$
\begin{align*}
P_{ivj} &= \frac{P(\text{at most one virus} \mid \text{Virus } v) \times P_v}{P(\text{at most one virus})} \\
        &= \frac{P(\text{Only Virus } v)}{P(\text{at most one virus})}
\end{align*}
$$

## Computing the Probabilities

The component probabilities are defined as:

$$
\begin{align*}
P(\text{Only Virus } V) &= P_v \times \prod_{m \neq V} (1 - P_m) \\
P(\text{at most one virus}) &= P(\text{None}) + \sum_{k \in \text{viruses}} P_k \times \prod_{m \neq k} (1 - P_m) \\
P(\text{None}) &= \prod_{k \in \text{viruses}} (1 - P_k)
\end{align*}
$$

This formulation ensures that viruses with **higher transmissibility** are
more likely to be acquired when competing with other variants.
