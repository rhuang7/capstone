def check(candidate):
    assert candidate(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert candidate(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
    assert candidate(['jack','john','mary'])==['kcaj','nhoj','yram']


def reverse_strings(lst):
    return [s[::-1] for s in lst]

check(reverse_strings)