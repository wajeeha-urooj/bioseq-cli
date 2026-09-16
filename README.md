# 🧬 BioSeq-CLI

### Bioinformatics Sequence Analysis Toolkit

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Biopython](https://img.shields.io/badge/Biopython-Bioinformatics-green)](https://biopython.org/)
[![Tests](https://img.shields.io/badge/Tests-Pytest-orange?logo=pytest)](https://pytest.org/)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wajeeha-urooj/bioseq-cli/blob/main/notebooks/BioSeq-CLI-Development.ipynb)

A reusable Python command-line toolkit for **protein FASTA sequence analysis, computational quality control, sequence statistics, and sequence diversity analysis**.

---

## 🚀 Try the Development Notebook

Explore and run the complete exploratory workflow in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wajeeha-urooj/bioseq-cli/blob/main/notebooks/BioSeq-CLI-Development.ipynb)

The notebook demonstrates the development and testing of BioSeq-CLI using a real protein FASTA dataset obtained from UniProt.

---

## 📌 Project Overview

**BioSeq-CLI** is a lightweight bioinformatics toolkit designed to automate common computational checks and analyses for protein FASTA datasets.

The project was first developed as an exploratory Jupyter Notebook and then converted into a modular Python command-line toolkit.

The toolkit can:

* 🧪 Parse FASTA and compressed FASTA (`.fasta.gz`) files
* 🔍 Detect empty sequences
* ⚠️ Identify unexpected amino-acid characters
* ♻️ Detect duplicate sequences
* 📏 Analyze protein sequence lengths
* 🧬 Calculate amino-acid composition
* 🎯 Filter sequences using user-defined length ranges
* 📊 Calculate Shannon entropy
* 📋 Generate sequence-level summaries
* 💻 Run analyses from the command line
* 🧪 Test core functions using Pytest

---

## 🧠 Why BioSeq-CLI?

Protein FASTA datasets often require basic computational inspection before being used in downstream bioinformatics analyses.

BioSeq-CLI provides a standardized and reusable workflow for these checks instead of requiring researchers to repeatedly write custom scripts for each dataset.

The toolkit separates **detection from automatic removal**.

For example, unusually short or long sequences are identified for inspection rather than automatically discarded. Similarly, unexpected amino-acid characters are reported rather than automatically treated as biological errors.

This allows researchers to apply filtering decisions according to the biological question and characteristics of their dataset.

---

## 🔬 Biological Dataset

The development workflow was tested using a real protein FASTA dataset obtained from **UniProt**.

The dataset used during development contains:

* **60 protein sequences**
* Protein FASTA format
* Reviewed UniProt records

The toolkit itself is **not restricted to this dataset**.

It can be applied to FASTA files containing:

* Different numbers of sequences
* Different protein datasets
* Different organisms
* Different protein families
* Researcher-generated sequence collections

The raw input dataset is not required to be stored in this repository. Users can provide their own FASTA or FASTA.GZ files.

---

## 🔄 Analysis Workflow

```text
              FASTA / FASTA.GZ
                     │
                     ▼
              Sequence Parsing
                     │
                     ▼
             Computational QC
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Empty     Unexpected   Duplicate
      Sequences  Characters   Sequences
          │          │          │
          └──────────┼──────────┘
                     ▼
             Sequence Statistics
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Length    Amino-Acid   Shannon
      Analysis   Composition  Entropy
          │          │          │
          └──────────┼──────────┘
                     ▼
             Optional Filtering
                     │
                     ▼
              Summary / Reports
```

---

## 🛠️ Technologies

| Technology      | Purpose                                        |
| --------------- | ---------------------------------------------- |
| 🐍 Python       | Core programming language                      |
| 🧬 Biopython    | FASTA parsing and biological sequence handling |
| 📊 Pandas       | Data organization in the development workflow  |
| 🔢 NumPy        | Numerical analysis in the notebook             |
| 📈 Matplotlib   | Data visualization                             |
| 🧪 Pytest       | Automated testing                              |
| 💻 Command Line | Reusable sequence analysis                     |

---

## 📂 Project Structure

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

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/wajeeha-urooj/bioseq-cli.git
cd bioseq-cli
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

## 💻 Command-Line Usage

BioSeq-CLI accepts both standard FASTA and compressed FASTA files.

### Analyze a FASTA file

```bash
python -m bioseq.cli protein_sequences.fasta
```

### Analyze a compressed FASTA file

```bash
python -m bioseq.cli protein_sequences.fasta.gz
```

The toolkit reports basic sequence statistics and amino-acid composition directly in the terminal.

---

## 📊 Example Output

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
E: ... residues (...%)
...
```

Values depend on the input FASTA dataset.

---

## 🧪 Testing

The project includes automated unit tests using **Pytest**.

Run the tests from the repository root:

```bash
pytest
```

The current test suite checks core functionality including:

* Sequence-length calculation
* Empty-sequence detection
* Duplicate-sequence detection
* Length-based filtering
* Shannon entropy calculation

---

## 📓 Development Notebook

The `notebooks/` directory contains the exploratory development workflow used to develop and evaluate the toolkit.

The notebook includes:

* FASTA input and parsing
* Sequence inspection
* Empty-sequence detection
* Unexpected-character detection
* Sequence-length analysis
* Sequence-length visualization
* Duplicate detection
* Amino-acid composition analysis
* Sequence-length filtering
* Shannon entropy calculation
* Sequence diversity analysis
* Dataset summary generation
* Result export

The notebook represents the **exploratory analysis stage**, while the `bioseq/` directory contains the reusable Python implementation.

---

## 🧩 Core Modules

### `bioseq/analyzer.py`

Contains the core sequence-analysis functions:

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
* FASTA.GZ input
* Sequence loading
* Execution of analysis functions
* Terminal output

### `tests/test_analyzer.py`

Contains automated tests for the core sequence-analysis functions.

---

## 🔬 Computational Quality Control

BioSeq-CLI treats computational quality control separately from biological interpretation.

For example:

**Unexpected characters**

The toolkit reports characters outside the standard amino-acid alphabet. It does not automatically assume that every non-standard character represents an invalid biological record.

**Sequence length**

Very short or very long sequences are reported or filtered according to user-defined criteria rather than being automatically classified as incorrect.

**Duplicate sequences**

Identical sequences are detected and reported without automatically deleting them.

This design allows researchers to retain control over decisions that depend on their specific biological research question.

---

## 🧪 Development Approach

The project was developed in two stages.

### Stage 1 — Exploratory Bioinformatics Analysis

The workflow was initially developed in a Jupyter Notebook using a real protein FASTA dataset.

This stage focused on:

* Understanding the input data
* Developing sequence-analysis functions
* Performing computational quality checks
* Exploring sequence characteristics
* Generating visualizations
* Producing summary results

### Stage 2 — Reusable Python Toolkit

The exploratory workflow was then converted into a modular Python project.

This stage introduced:

* Reusable functions
* Modular project structure
* Command-line execution
* Automated testing
* Dependency management
* Documentation

This transition demonstrates how an exploratory bioinformatics analysis can be converted into a reusable computational tool.

---

## 📈 Project Outputs

The development workflow generates several useful outputs, including:

* Protein sequence length statistics
* Sequence-length distributions
* Amino-acid composition
* Duplicate-sequence information
* Sequence diversity measurements
* Sequence-level summary tables
* Automated text reports
* CSV result files

---

## 🔮 Future Development

Planned improvements include:

* ⚙️ More flexible command-line arguments
* 📤 Direct result export from the CLI
* 🧬 FASTA output for filtered sequences
* 🔬 Additional protein sequence descriptors
* 🛡️ Improved input validation and error handling
* 🧪 Expanded automated test coverage
* 📦 Standard Python package installation
* 📊 Additional sequence visualizations

---

## 👩‍💻 Author

**Wajeeha Urooj**

MPhil Bioinformatics

This project demonstrates practical experience in:

**Python • Bioinformatics • Computational Biology • Protein Sequence Analysis • Data Processing • Reproducible Workflows • Command-Line Tools • Software Testing**
