from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from bioseq.analyzer import (
    calculate_sequence_lengths,
    find_empty_sequences,
    find_unexpected_characters,
    find_duplicate_sequences,
    calculate_amino_acid_composition,
    filter_by_length,
    sequence_entropy,
    calculate_sequence_entropy,
)


def make_test_records():
    """Create small test records for unit testing."""
    return [
        SeqRecord(Seq("MKTLLA"), id="protein_1"),
        SeqRecord(Seq("MKTLLA"), id="protein_2"),
        SeqRecord(Seq("ACDEFG"), id="protein_3"),
        SeqRecord(Seq(""), id="empty"),
    ]


def test_calculate_sequence_lengths():
    records = make_test_records()

    lengths = calculate_sequence_lengths(records)

    assert lengths == [6, 6, 6, 0]


def test_find_empty_sequences():
    records = make_test_records()

    empty = find_empty_sequences(records)

    assert empty == ["empty"]


def test_find_unexpected_characters():
    records = [
        SeqRecord(Seq("MKTLLA"), id="valid"),
        SeqRecord(Seq("MKTLLX"), id="invalid"),
    ]

    result = find_unexpected_characters(records)

    assert result["invalid"] == ["X"]


def test_find_duplicate_sequences():
    records = make_test_records()

    duplicates = find_duplicate_sequences(records)

    assert len(duplicates) == 1
    assert duplicates["MKTLLA"] == ["protein_1", "protein_2"]


def test_calculate_amino_acid_composition():
    records = [
        SeqRecord(Seq("AAAA"), id="protein_1"),
        SeqRecord(Seq("CCCC"), id="protein_2"),
    ]

    result = calculate_amino_acid_composition(records)

    assert result["A"]["count"] == 4
    assert result["C"]["count"] == 4
    assert result["A"]["percentage"] == 50.0
    assert result["C"]["percentage"] == 50.0


def test_filter_by_length():
    records = make_test_records()

    filtered = filter_by_length(
        records,
        min_length=6,
        max_length=6,
    )

    assert len(filtered) == 3
    assert [record.id for record in filtered] == [
        "protein_1",
        "protein_2",
        "protein_3",
    ]


def test_sequence_entropy():
    entropy = sequence_entropy("AAAA")

    assert entropy == 0.0


def test_calculate_sequence_entropy():
    records = [
        SeqRecord(Seq("AAAA"), id="low_entropy"),
        SeqRecord(Seq("ACDE"), id="higher_entropy"),
    ]

    result = calculate_sequence_entropy(records)

    assert result["low_entropy"] == 0.0
    assert result["higher_entropy"] > 0.0
    
