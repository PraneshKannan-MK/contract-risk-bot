from preprocessing.clause_segmenter import segment_clauses


def test_clause_segmentation():
    text = """
    1. Termination
    Either party may terminate with notice.

    2. Payment
    Payment shall be made within 30 days.
    """
    clauses = segment_clauses(text)
    assert len(clauses) >= 2