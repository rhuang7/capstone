def check(candidate):
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
    assert candidate(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']


def extract_strings_by_length(strings, length):
    return [s for s in strings if len(s) == length]

check(extract_strings_by_length)