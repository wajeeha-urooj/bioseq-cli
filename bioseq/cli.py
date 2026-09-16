import argparse
import gzip

from Bio import SeqIO

from .analyzer import (
    calculate_sequence_lengths,
    find_empty_sequences,
    find_unexpected_characters,
    find_duplicate_sequences,
    calculate_amino_acid_composition,
)


def load_fasta(filename):
    """Load protein sequences from FASTA or FASTA.GZ."""
    if filename.endswith(".gz"):
        with gzip.open(filename, "rt") as handle:
            return list(SeqIO.parse(handle, "fasta"))

    with open(filename, "r") as handle:
        return list(SeqIO.parse(handle, "fasta"))


def main():
    parser = argparse.ArgumentParser(
        description="BioSeq-CLI: Bioinformatics Sequence Analysis Toolkit"
    )

    parser.add_argument(
        "fasta",
        help="Input FASTA or FASTA.GZ file"
    )

    args = parser.parse_args()

    records = load_fasta(args.fasta)

    lengths = calculate_sequence_lengths(records)
    empty_sequences = find_empty_sequences(records)
    invalid_sequences = find_unexpected_characters(records)
    duplicate_groups = find_duplicate_sequences(records)

    print("\nBioSeq-CLI Sequence Analysis")
    print("=" * 40)

    print(f"Total sequences: {len(records)}")
    print(f"Mean sequence length: {sum(lengths) / len(lengths):.2f} aa")
    print(f"Minimum length: {min(lengths)} aa")
    print(f"Maximum length: {max(lengths)} aa")
    print(f"Empty sequences: {len(empty_sequences)}")
    print(
        f"Sequences with unexpected characters: "
        f"{len(invalid_sequences)}"
    )
    print(f"Duplicate sequence groups: {len(duplicate_groups)}")

    print("\nAmino-Acid Composition")
    print("-" * 40)

    composition = calculate_amino_acid_composition(records)

    for amino_acid, values in composition.items():
        print(
            f"{amino_acid}: "
            f"{values['count']} residues "
            f"({values['percentage']:.2f}%)"
        )


if __name__ == "__main__":
    main()
