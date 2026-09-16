from collections import Counter, defaultdict
import math


STANDARD_AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")


def calculate_sequence_lengths(records):
    """Return sequence lengths for a collection of FASTA records."""
    return [len(record.seq) for record in records]


def find_empty_sequences(records):
    """Return IDs of sequences with zero length."""
    return [
        record.id
        for record in records
        if len(record.seq) == 0
    ]


def find_unexpected_characters(records):
    """Return sequence IDs and unexpected characters."""
    invalid_sequences = {}

    for record in records:
        sequence = str(record.seq).upper()
        unexpected = set(sequence) - STANDARD_AMINO_ACIDS

        if unexpected:
            invalid_sequences[record.id] = sorted(unexpected)

    return invalid_sequences


def find_duplicate_sequences(records):
    """Identify groups of records with identical sequences."""
    sequence_groups = defaultdict(list)

    for record in records:
        sequence = str(record.seq).upper()
        sequence_groups[sequence].append(record.id)

    return {
        sequence: ids
        for sequence, ids in sequence_groups.items()
        if len(ids) > 1
    }


def calculate_amino_acid_composition(records):
    """Calculate amino-acid counts and percentages."""
    amino_acid_counts = Counter()

    for record in records:
        sequence = str(record.seq).upper()
        amino_acid_counts.update(sequence)

    total_residues = sum(
        amino_acid_counts[aa]
        for aa in STANDARD_AMINO_ACIDS
    )

    composition = {}

    for aa in sorted(STANDARD_AMINO_ACIDS):
        count = amino_acid_counts[aa]
        percentage = (
            count / total_residues * 100
            if total_residues > 0
            else 0
        )

        composition[aa] = {
            "count": count,
            "percentage": percentage
        }

    return composition


def filter_by_length(records, min_length=50, max_length=2000):
    """Return sequences within a user-defined length range."""
    return [
        record
        for record in records
        if min_length <= len(record.seq) <= max_length
    ]


def sequence_entropy(sequence):
    """Calculate Shannon entropy of a protein sequence."""
    counts = Counter(sequence)
    length = len(sequence)

    if length == 0:
        return 0.0

    entropy = 0.0

    for count in counts.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy


def calculate_sequence_entropy(records):
    """Calculate Shannon entropy for each sequence."""
    return {
        record.id: sequence_entropy(str(record.seq).upper())
        for record in records
    }
