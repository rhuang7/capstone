import sys
from math import factorial
from itertools import permutations

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def count_valid_sequences(s):
        n = len(s)
        total = factorial(n)
        forbidden = 0

        # Count permutations containing "kar"
        k = s.find('k')
        a = s.find('a')
        r = s.find('r')
        if k != -1 and a != -1 and r != -1:
            # Number of permutations where 'k' is before 'a' and 'a' is before 'r'
            # Choose positions for k, a, r in order
            # Total permutations with "kar" as a subsequence
            # We fix k, a, r in order and permute the rest
            # Number of ways to choose positions for k, a, r: C(n,3)
            # Then multiply by 1 (for fixed order) and by (n-3)! for the rest
            # But since we want exact occurrences, we need to count permutations where "kar" appears as a subsequence
            # So total permutations with "kar" = (n-3)! * (number of ways to choose positions for k, a, r in order)
            # Which is (n-3)! * 1 (since k, a, r must be in order)
            # So total is (n-3)! * 1
            # But we also have to consider that "kar" can appear in multiple ways
            # So we use inclusion-exclusion
            # First count permutations containing "kar" as a subsequence
            # Then subtract permutations containing "shi" as a subsequence
            # Then add back permutations containing both "kar" and "shi" as subsequences
            # So we use inclusion-exclusion
            # But for this problem, we can directly compute the number of permutations that contain "kar" or "shi" as a subsequence
            # So we use inclusion-exclusion
            # First count permutations containing "kar" as a subsequence
            # Then count permutations containing "shi" as a subsequence
            # Then subtract permutations containing both
            # So the formula is:
            # total_valid = total - (count_kar + count_shi - count_both)
            # So we need to compute count_kar, count_shi, count_both

            # Count permutations containing "kar" as a subsequence
            count_kar = 0
            # Find indices of k, a, r in the string
            k_pos = s.find('k')
            a_pos = s.find('a')
            r_pos = s.find('r')
            if k_pos != -1 and a_pos != -1 and r_pos != -1:
                # Number of ways to choose positions for k, a, r in order
                # Choose 3 positions out of n, then arrange k, a, r in order
                # The rest can be arranged freely
                # So total is C(n,3) * (n-3)!
                # Which is n! / (3! * (n-3)!) ) * (n-3)! ) = n! / 3!
                count_kar = factorial(n) // factorial(3)

            # Count permutations containing "shi" as a subsequence
            count_shi = 0
            s_pos = s.find('s')
            h_pos = s.find('h')
            i_pos = s.find('i')
            if s_pos != -1 and h_pos != -1 and i_pos != -1:
                count_shi = factorial(n) // factorial(3)

            # Count permutations containing both "kar" and "shi" as subsequences
            count_both = 0
            # Check if all characters in "kar" and "shi" are present
            if k_pos != -1 and a_pos != -1 and r_pos != -1 and s_pos != -1 and h_pos != -1 and i_pos != -1:
                # Number of ways to choose positions for k, a, r, s, h, i in order
                # Choose 6 positions out of n, then arrange k, a, r, s, h, i in order
                # The rest can be arranged freely
                # So total is C(n,6) * (n-6)! ) = n! / (6! * (n-6)! )) * (n-6)! ) = n! / 6!
                count_both = factorial(n) // factorial(6)

            # Inclusion-exclusion
            total_invalid = count_kar + count_shi - count_both
            return total - total_invalid
        return total

    for s in cases:
        print(count_valid_sequences(s))

if __name__ == '__main__':
    solve()