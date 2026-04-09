# Examples

This section is for runnable code rather than narrative explanation.

## What Lives Here

- Upstream examples synced from the main
  [UofUEpiBio/epiworld](https://github.com/UofUEpiBio/epiworld) repository.
- Showcase files such as `helloworld.cpp` and `readme.cpp`.
- A stable landing page even when the upstream source has not been cloned
  locally yet.

## How The Gallery Is Built

During CI and local development, `scripts/sync_examples.py` scans
`epiworld-src/` and generates a browsable gallery under
[Repository Gallery](repository/index.md).

This keeps example code maintained in one place while still making it easy to
read on the docs site.
