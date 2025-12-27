def check(candidate):
    assert candidate([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert candidate([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert candidate([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}


def count_similar_occurrences(records):
    from collections import Counter

    # Count occurrences of each record
    occurrence_count = Counter(records)

    # Create a dictionary to hold similar occurrences
    similar_occurrences = {}

    # Iterate through the occurrence counts
    for record, count in occurrence_count.items():
        # Find all records with the same occurrence count
        similar_records = [r for r, c in occurrence_count.items() if c == count and r != record]
        similar_occurrences[record] = similar_records

    return similar_occurrences

check(count_similar_occurrences)