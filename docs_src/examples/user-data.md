# User Data Collection

*Source:
[`examples/05-user-data`](https://github.com/UofUEpiBio/epiworld/tree/master/examples/05-user-data)*

This example shows how to use `set_user_data()` and `add_user_data()` to
record custom per-event information during a simulation. Here, the
post-recovery function logs the agent ID and virus ID whenever an agent
recovers.

## Source Code

```cpp
#include "epiworld.hpp"

int main()
{
    epiworld::Model<> model;
    model.add_state("Susceptible", epiworld::default_update_susceptible<>);
    auto exposed_state = model.add_state(
        "Exposed", epiworld::default_update_exposed<>);
    auto removed_state = model.add_state("Removed");

    // Declare user-data columns
    model.set_user_data({"agent_id", "virus_id"});

    model.agents_from_adjlist(
        epiworld::rgraph_smallworld(200, 5, .1, false, model)
    );

    model.add_param(.9, "infectiousness");
    model.add_param(.3, "recovery");

    // Virus with a post-recovery hook
    epiworld::Virus<> v("covid", 5, false);
    v.set_state(exposed_state, removed_state, removed_state);

    EPI_NEW_POSTRECOVERYFUN_LAMBDA(immunity, int)
    {
        p->add_tool(*m, *m->get_tools()[1u]);
        m->add_user_data({
            static_cast< epiworld_double >(p->get_id()),
            static_cast< epiworld_double >(v.get_id())
        });
    };

    v.set_post_recovery(immunity);
    v.set_prob_infecting("infectiousness");

    // Tools
    epiworld::Tool<> is("immune system", 1.0, true);
    is.set_susceptibility_reduction(.3);
    is.set_death_reduction(.9);
    is.set_recovery_enhancer("recovery");

    epiworld::Tool<> postImm("post immunity", 0, false);
    postImm.set_susceptibility_reduction(1.0);

    model.add_tool(is);
    model.add_tool(postImm);
    model.add_virus(v);
    model.run(112, 30);
    model.print();

    model.get_user_data().print();
    model.get_user_data().write("user-data.txt");
}
```

## Key Takeaways

- `set_user_data(column_names)` declares custom columns before the simulation.
- Inside a post-recovery function, `add_user_data()` appends a row of values.
- After the run, `get_user_data().print()` or `.write()` exports the table.
