# BioSeq-CLI: Bioinformatics Sequence Analysis Toolkit

A reusable Python command-line toolkit for analyzing and performing basic quality checks on protein FASTA sequence datasets.

## Overview

**BioSeq-CLI** is a lightweight bioinformatics toolkit designed to automate common sequence-analysis and data-quality checks for protein FASTA files.

The project was developed as a practical bioinformatics workflow using a real protein sequence dataset and then converted from an exploratory Jupyter Notebook into a modular Python command-line application.

The toolkit is designed to work with FASTA files from sources such as UniProt, NCBI, sequencing projects, laboratory datasets, or other biological sequence collections.

## Why BioSeq-CLI?

Protein FASTA datasets often require basic inspection before they are used in downstream computational analyses.

BioSeq-CLI provides a standardized way to perform these checks rather than repeatedly writing custom scripts for each dataset.

The toolkit can help researchers identify:

* Empty sequences
* Unexpected amino-acid characters
* Duplicate sequences
* Unusual sequence lengths
* Amino-acid composition patterns
* Sequence diversity using Shannon entropy
* Sequences meeting user-defined length criteria

The original input dataset is not automatically modified during quality-control analysis. Detection and filtering are kept as separate operations so that researchers can make decisions appropriate to their specific analysis.

## Features

* FASTA and compressed FASTA (`.fasta.gz`) input
* Sequence parsing using Biopython
* Sequence-length statistics
* Empty-sequence detection
* Unexpected-character detection
* Duplicate-sequence detection
* Amino-acid composition analysis
* User-defined sequence-length filtering
* Shannon entropy calculation
* Sequence-level summary generation
* Command-line interface
* Automated unit tests
* CSV and text-based result export in the development workflow

## Project Workflow

```text
FASTA Input
    ↓
Sequence Parsing
    ↓
Quality Checks
    ├── Empty Sequences
    ├── Unexpected Characters
    ├── Duplicate Sequences
    └── Sequence Length
    ↓
Sequence Analysis
    ├── Amino-Acid Composition
    ├── Length Filtering
    └── Shannon Entropy
    ↓
Summary and Reports
```

## Dataset

The development workflow was tested using a real protein FASTA dataset obtained from UniProt.

The dataset contains **60 protein sequences** and was used to demonstrate the toolkit on realistic biological sequence data.

The toolkit itself is **not restricted to this dataset**, human proteins, or a fixed number of sequences. Users can provide their own FASTA or FASTA.GZ files.

The raw input dataset is not required to be included in this repository. Users can provide their own biological sequence files.

## Installation

Clone the repository:

```bash
git clone https://github.com/wajeeha-urooj/bioseq-cli.git
cd bioseq-cli
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

BioSeq-CLI accepts a FASTA or compressed FASTA file as input.

For a FASTA file:

```bash
python -m bioseq.cli protein_sequences.fasta
```

For a compressed FASTA file:

```bash
python -m bioseq.cli protein_sequences.fasta.gz
```

The command-line program reports basic dataset statistics and amino-acid composition directly in the terminal.

## Example Output

```text
BioSeq-CLI Sequence Analysis
========================================
Total sequences: 60
Mean sequence length: ...
Minimum length: ...
Maximum length: ...
Empty sequences: 0
Sequences with unexpected characters: ...
Duplicate sequence groups: ...

Amino-Acid Composition
----------------------------------------
A: ... residues (...%)
C: ... residues (...%)
D: ... residues (...%)
...
```

Values depend on the input FASTA dataset.

## Repository Structure

```text
bioseq-cli/
│
├── bioseq/
│   ├── __init__.py
│   ├── analyzer.py
│   └── cli.py
│
├── notebooks/
│   └── BioSeq-CLI-Development.ipynb
│
├── tests/
│   └── test_analyzer.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Module Description

### `bioseq/analyzer.py`

Contains the core sequence-analysis functions, including:

* Sequence-length calculation
* Empty-sequence detection
* Unexpected-character detection
* Duplicate detection
* Amino-acid composition
* Length-based filtering
* Shannon entropy

### `bioseq/cli.py`

Provides the command-line interface and handles:

* FASTA input
* Compressed FASTA input
* Sequence loading
* Execution of analysis functions
* Terminal reporting

### `tests/test_analyzer.py`

Contains automated tests for important sequence-analysis functions using small controlled test records.

## Testing

The project includes unit tests using `pytest`.

Run the tests from the repository root:

```bash
pytest
```

The tests verify core functionality such as:

* Sequence-length calculation
* Empty-sequence detection
* Duplicate detection
* Length filtering
* Shannon entropy calculation

## Technologies

* **Python**
* **Biopython**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Pytest**
* **FASTA**
* **Command-line interfaces**
* **Sequence analysis**
* **Computational biology**

## Biological and Computational Considerations

BioSeq-CLI separates computational quality checks from biological interpretation.

For example, an unexpected character in a protein sequence is reported rather than automatically treated as an erroneous biological record. Likewise, unusually short or long sequences are identified for inspection rather than automatically removed.

This approach allows the researcher to apply filtering criteria according to the biological question and dataset requirements.

## Development Approach

The project was developed in two stages.

### Stage 1 — Exploratory Development

The workflow was initially developed and tested in a Jupyter Notebook using a real protein FASTA dataset.

This stage focused on:

* Understanding the input data
* Developing sequence-analysis functions
* Inspecting data quality
* Visualizing sequence characteristics
* Generating summary results

### Stage 2 — Reusable Toolkit

The notebook workflow was then converted into a modular Python project.

This stage introduced:

* Reusable Python functions
* A command-line interface
* Automated testing
* Dependency management
* Project organization
* Documentation

This development process demonstrates the transition from exploratory bioinformatics analysis to a reusable computational tool.

## Future Development

Planned improvements include:

* More flexible command-line options
* Exporting analysis results directly from the CLI
* Additional protein sequence descriptors
* FASTA output for filtered sequences
* Improved validation and error handling
* Support for additional sequence-analysis workflows
* Package installation through standard Python packaging tools

## Author

**Wajeeha Urooj**

MPhil Bioinformatics

This project was developed as part of a bioinformatics portfolio demonstrating Python programming, computational biology, sequence analysis, reproducible workflows, and software development practices.
