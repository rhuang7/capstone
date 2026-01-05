import sys
from math import factorial

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:]

    def count_valid_permutations(s):
        n = len(s)
        total = factorial(n)
        # Count permutations containing "kar"
        kar_count = 0
        # Treat "kar" as a single entity, so we have (n-3) + 1 = n-2 elements
        # Number of ways to arrange these elements: (n-2)! * 1 (for "kar")
        kar_count = factorial(n-3) * 1
        # Count permutations containing "shi"
        shi_count = factorial(n-3) * 1
        # Count permutations containing both "kar" and "shi"
        # Treat both as single entities, so we have (n-3-3) + 2 = n-4 elements
        # Number of ways to arrange these elements: (n-4)! * 1 * 1
        both_count = factorial(n-6) * 1 * 1 if n >= 6 else 0
        # Use inclusion-exclusion principle
        valid = total - kar_count - shi_count + both_count
        return valid

    for s in cases:
        print(count_valid_permutations(s))

if __name__ == '__main__':
    solve()