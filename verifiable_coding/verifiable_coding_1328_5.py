import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def min_ops(s):
        n = len(s)
        min_ops = float('inf')

        # Generate all possible lucky numbers with the same length as s
        from itertools import product
        for digits in product(['4', '7'], repeat=n):
            lucky = ''.join(digits)
            ops = 0
            for a, b in zip(s, lucky):
                if a != b:
                    ops += 1
            min_ops = min(min_ops, ops)

        # Generate all possible lucky numbers with length +1
        for digits in product(['4', '7'], repeat=n+1):
            lucky = ''.join(digits)
            ops = 0
            for a, b in zip(s, lucky):
                if a != b:
                    ops += 1
            min_ops = min(min_ops, ops)

        return min_ops

    for case in cases:
        print(min_ops(case))

if __name__ == '__main__':
    solve()