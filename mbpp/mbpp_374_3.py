def check(candidate):
    assert candidate('ab')==['ab', 'ba']
    assert candidate('abc')==['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    assert candidate('abcd')==['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']


def print_permutations(s):
    from itertools import permutations
    
    # Generate all permutations of the string
    perms = permutations(s)
    
    # Convert each permutation tuple to a string and print it
    for p in perms:
        print(''.join(p))

check(print_permutations)