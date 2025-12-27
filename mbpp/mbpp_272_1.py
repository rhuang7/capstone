def check(candidate):
    assert candidate([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
    assert candidate([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
    assert candidate([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]


def extract_rear_element(records):
    if not records:
        return None
    return records[-1][1]

check(extract_rear_element)