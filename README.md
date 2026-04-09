# Epiworld Documentation

[![MkDocs Documentation](https://github.com/UofUEpiBio/epiworld-docs/actions/workflows/doxy-action.yml/badge.svg)](https://github.com/UofUEpiBio/epiworld-docs/actions/workflows/doxy-action.yml)

This repository hosts the documentation website for the
[**epiworld**](https://github.com/UofUEpiBio/epiworld) C++ library — a fast,
general-purpose framework for agent-based epidemiological simulation.

**Live site:** <https://UofUEpiBio.github.io/epiworld-docs>

## Repository Structure

```
epiworld-docs/
├── docs_src/              # Documentation source (mkdocs content)
│   ├── README.md          # Homepage
│   ├── guide/             # User Guide chapters (fundamentals, building models, etc.)
│   ├── concepts/          # Core theory (simulation steps, agents, contagion)
│   ├── models/            # Built-in model documentation
│   ├── examples/          # Runnable examples from the epiworld repository
│   ├── advanced/          # Advanced topics (architecture, performance, etc.)
│   ├── impl/              # Implementation details
│   ├── api/               # API reference overview
│   ├── assets/            # Images and branding
│   └── javascripts/       # MathJax configuration
├── mkdocs.yml             # MkDocs configuration
└── .github/workflows/     # CI/CD pipeline
```

The documentation is organized into three main parts:

1. **User Guide** — Step-by-step chapters covering fundamentals, building
   custom models, adding viruses/tools/events, and the built-in models.
2. **Examples** — Runnable C++ examples from the epiworld repository.
3. **API Reference** — Complete class and function reference generated from
   the source code via Doxygen.

## How It Works

The documentation website is built with [MkDocs](https://www.mkdocs.org/) and
the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.
API reference documentation is generated from the epiworld source code using
[mkdoxy](https://github.com/JakubAndrysek/MkDoxy) (Doxygen + MkDocs
integration).

**Important:** This repository does **not** contain the epiworld source code.
During the build process, the CI workflow clones the
[epiworld repository](https://github.com/UofUEpiBio/epiworld) to access the
latest Doxygen comments for API documentation generation.

## Local Development

To build the documentation locally:

```bash
# Clone the epiworld source for API docs
git clone --depth 1 https://github.com/UofUEpiBio/epiworld.git epiworld-src

# Install dependencies
pip install mkdocs mkdocs-material mkdoxy
sudo apt-get install -y doxygen graphviz  # or use brew on macOS

# Build and serve locally
mkdocs serve
```

Then visit <http://127.0.0.1:8000> in your browser.

## Contributing

Contributions to the documentation are welcome! Please open an issue or pull
request in this repository. For changes to the epiworld library itself, please
contribute to the [main repository](https://github.com/UofUEpiBio/epiworld).

## License

See [LICENSE.md](LICENSE.md) for details.
