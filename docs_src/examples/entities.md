# Entities and Population Mixing

*Source:
[`examples/11-entities`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/11-entities)*

This example demonstrates how to use **entities** and a **contact matrix** to
model heterogeneous mixing between population groups. It uses `ModelSEIRMixing`
with three entities and a 3×3 contact matrix.

## Source Code

```cpp
#include "epiworld.hpp"

using namespace epiworld;

template<typename TSeq = EPI_DEFAULT_TSEQ>
EntityToAgentFun<TSeq> dist_factory(size_t from, size_t to) {
    return [from, to](Entity<> & e, Model<> * m) -> void {
        auto & agents = m->get_agents();
        for (size_t i = from; i < to; ++i)
            e.add_agent(&agents[i], *m);
    };
}

int main() {

    std::vector< double > contact_matrix = {
        0.9, 0.1, 0.1,
        0.05, 0.8, .2,
        0.05, 0.1, 0.7
    };

    epimodels::ModelSEIRMixing<> model(
        "Flu",     // Virus name
        10000,     // Population size
        0.01,      // Initial prevalence
        10.0,      // Contact rate
        0.1,       // Transmission rate
        4.0,       // Avg incubation days
        1.0/7.0,   // Recovery rate
        contact_matrix
    );

    // Three population groups
    Entity<> e1("Entity 1", dist_factory<>(0, 3000));
    Entity<> e2("Entity 2", dist_factory<>(3000, 6000));
    Entity<> e3("Entity 3", dist_factory<>(6000, 10000));

    model.add_entity(e1);
    model.add_entity(e2);
    model.add_entity(e3);

    // Run
    model.run(50, 123);
    model.print();

    return 0;
}
```

## Key Takeaways

- **Entities** represent population groups (e.g., schools, workplaces,
  age classes).
- A **contact matrix** specifies the relative contact rates between groups.
- `dist_factory` is a helper that assigns agents to entities by index range.
- The `ModelSEIRMixing` model handles the mixing logic internally based on
  entity membership and the contact matrix.
