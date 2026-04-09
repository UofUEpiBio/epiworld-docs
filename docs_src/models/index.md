# Models

Epiworld ships with a collection of pre-built epidemiological models that cover
common transmission patterns. Each model can be used out of the box or
customized to fit specific research questions.

## How Models Are Organized

Models are grouped by their compartmental structure and population mixing
assumptions:

### Basic Compartmental Models

Standard compartmental models operating on network-based contact structures:

| Model | Description |
|-------|-------------|
| [SIS](../epiworld/classModelSIS.md) | Susceptible ↔ Infected (no permanent immunity) |
| [SIR](../epiworld/classModelSIR.md) | Susceptible → Infected → Recovered |
| [SEIR](../epiworld/classModelSEIR.md) | Adds an Exposed compartment to SIR |

### Models with Death Compartment

Extensions that include a death/removed compartment:

| Model | Description |
|-------|-------------|
| [SIRD](../epiworld/classModelSIRD.md) | SIR with Death |
| [SISD](../epiworld/classModelSISD.md) | SIS with Death |
| [SEIRD](../epiworld/classModelSEIRD.md) | SEIR with Death |

### Connected Population Models

Models where the entire population is assumed to be connected (mean-field
approximation):

| Model | Description |
|-------|-------------|
| [SIR Connected](../epiworld/classModelSIRCONN.md) | Fully connected SIR |
| [SEIR Connected](../epiworld/classModelSEIRCONN.md) | Fully connected SEIR |
| [SIRD Connected](../epiworld/classModelSIRDCONN.md) | Fully connected SIRD |
| [SEIRD Connected](../epiworld/classModelSEIRDCONN.md) | Fully connected SEIRD |

### Population Mixing Models

Models with heterogeneous contact rates across population groups:

| Model | Description |
|-------|-------------|
| [SIR Mixing](../epiworld/classModelSIRMixing.md) | SIR with contact matrices |
| [SEIR Mixing](../epiworld/classModelSEIRMixing.md) | SEIR with contact matrices |
| [SEIR Mixing Quarantine](../epiworld/classModelSEIRMixingQuarantine.md) | SEIR mixing with quarantine |

### Disease-Specific Models

Detailed models tailored to specific diseases:

| Model | Description |
|-------|-------------|
| [Measles School](../epiworld/classModelMeaslesSchool.md) | Measles in school settings |
| [Measles Mixing](measles-mixing.md) | Measles with population mixing |
| [Measles Mixing Risk Quarantine](measles-mixing-risk-quarantine.md) | Measles with risk-stratified quarantine |

### Specialized Models

Models with unique features:

| Model | Description |
|-------|-------------|
| [SIR Logit](../epiworld/classModelSIRLogit.md) | SIR with logistic regression-based transmission |
| [Diffusion Network](../epiworld/classModelDiffNet.md) | Network diffusion model |
| [Surveillance](../epiworld/classModelSURV.md) | Model with surveillance components |
