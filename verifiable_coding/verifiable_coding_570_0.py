import sys
from math import factorial

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def count_valid_permutations(s):
        n = len(s)
        total = factorial(n)
        # Count permutations containing "kar"
        k = s.find('k')
        a = s.find('a')
        r = s.find('r')
        if k != -1 and a != -1 and r != -1 and k < a < r:
            # Count permutations where 'k' is before 'a' and 'a' is before 'r'
            count_kar = factorial(n - 3) * 1  # 1 way to arrange k, a, r in order
            total -= count_kar
        # Count permutations containing "shi"
        s = s.find('s')
        h = s.find('h')
        i = s.find('i')
        if s != -1 and h != -1 and i != -1 and s < h < i:
            # Count permutations where 's' is before 'h' and 'h' is before 'i'
            count_shi = factorial(n - 3) * 1  # 1 way to arrange s, h, i in order
            total -= count_shi
        # Subtract overlap (permutations containing both "kar" and "shi")
        # Check if both phrases can be present
        k = s.find('k')
        a = s.find('a')
        r = s.find('r')
        s2 = s.find('s')
        h2 = s.find('h')
        i2 = s.find('i')
        if k != -1 and a != -1 and r != -1 and s2 != -1 and h2 != -1 and i2 != -1:
            # Check if "kar" and "shi" can be in the string without overlapping
            # Check if 'k' < 'a' < 'r' and 's' < 'h' < 'i'
            if k < a < r and s2 < h2 < i2:
                # Count permutations where both "kar" and "shi" are present
                # Treat "kar" and "shi" as blocks
                # Total ways = (n - 6 + 2)! * 2! (ways to arrange the two blocks)
                # But since "kar" and "shi" are fixed in order, it's (n - 6)! * 1 * 1
                count_both = factorial(n - 6) * 1 * 1
                total -= count_both
        return total

    for s in cases:
        print(count_valid_permutations(s))

if __name__ == '__main__':
    main()