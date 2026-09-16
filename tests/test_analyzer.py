from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from bioseq.analyzer import (
    calculate_sequence_lengths,
    find_empty_sequences,
    find_unexpected_characters,
    find_duplicate_sequences,
    filter_by_length,
    sequence_entropy,
)


def make_test_records():
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


def test_find_duplicate_sequences():
    records = make_test_records()

    duplicates = find_duplicate_sequences(records)

    assert len(duplicates) == 1


def test_filter_by_length():
    records = make_test_records()

    filtered = filter_by_length(
        records,
        min_length=6,
        max_length=6
    )

    assert len(filtered) == 3


def test_sequence_entropy():
    entropy = sequence_entropy("AAAA")

    assert entropy == 0.0
