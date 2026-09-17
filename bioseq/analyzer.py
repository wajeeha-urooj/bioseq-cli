import argparse
import gzip

from Bio import SeqIO

from .analyzer import (
    calculate_sequence_lengths,
    find_empty_sequences,
    find_unexpected_characters,
    find_duplicate_sequences,
    calculate_amino_acid_composition,
    calculate_sequence_entropy,
)


def load_fasta(filename):
    """Load protein sequences from FASTA or FASTA.GZ."""
    try:
        if filename.endswith(".gz"):
            with gzip.open(filename, "rt") as handle:
                return list(SeqIO.parse(handle, "fasta"))

        with open(filename, "r") as handle:
            return list(SeqIO.parse(handle, "fasta"))

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {filename}")

    except OSError as error:
        raise OSError(f"Could not read input file: {error}")


def main():
    parser = argparse.ArgumentParser(
        description="BioSeq-CLI: Bioinformatics Sequence Analysis Toolkit"
    )

    parser.add_argument(
        "fasta",
        help="Input protein FASTA or FASTA.GZ file",
    )

    args = parser.parse_args()

    try:
        records = load_fasta(args.fasta)

        if not records:
            print("Error: No sequences were found in the input FASTA file.")
            return

        lengths = calculate_sequence_lengths(records)
        empty_sequences = find_empty_sequences(records)
        invalid_sequences = find_unexpected_characters(records)
        duplicate_groups = find_duplicate_sequences(records)
        composition = calculate_amino_acid_composition(records)
        entropy_values = calculate_sequence_entropy(records)

        mean_length = sum(lengths) / len(lengths)

        print("\nBioSeq-CLI Sequence Analysis")
        print("=" * 50)

        print(f"Total sequences: {len(records)}")
        print(f"Mean sequence length: {mean_length:.2f} aa")
        print(f"Minimum length: {min(lengths)} aa")
        print(f"Maximum length: {max(lengths)} aa")
        print(f"Empty sequences: {len(empty_sequences)}")
        print(
            f"Sequences with unexpected characters: "
            f"{len(invalid_sequences)}"
        )
        print(f"Duplicate sequence groups: {len(duplicate_groups)}")

        print("\nAmino-Acid Composition")
        print("-" * 50)

        for amino_acid, values in composition.items():
            print(
                f"{amino_acid}: "
                f"{values['count']} residues "
                f"({values['percentage']:.2f}%)"
            )

        print("\nSequence Entropy")
        print("-" * 50)

        entropy_values_list = list(entropy_values.values())

        mean_entropy = (
            sum(entropy_values_list) / len(entropy_values_list)
            if entropy_values_list
            else 0.0
        )

        print(f"Mean Shannon entropy: {mean_entropy:.4f}")

        print("\nAnalysis completed successfully.")

    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
