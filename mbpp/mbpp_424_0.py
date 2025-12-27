def check(candidate):
    assert candidate(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert candidate(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert candidate(('Gotta', 'get', 'go') ) == ['a', 't', 'o']


def extract_rear_elements(tup):
    return [s[-1] for s in tup if isinstance(s, str)]

check(extract_rear_elements)