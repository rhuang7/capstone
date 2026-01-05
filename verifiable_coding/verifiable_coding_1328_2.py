import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def min_ops(n_str):
        n = int(n_str)
        min_ops = float('inf')

        # Check all possible lucky numbers up to 10^100000 (since N can be up to 1e100000)
        # Generate all lucky numbers with length equal to len(n_str) or less
        # But since N can be very large, we need a smarter approach

        # Generate all lucky numbers with the same number of digits as n_str
        from itertools import product
        digits = ['4', '7']
        for bits in product(digits, repeat=len(n_str)):
            lucky = ''.join(bits)
            if lucky[0] == '0':
                continue
            ops = 0
            for i in range(len(n_str)):
                if n_str[i] != lucky[i]:
                    ops += 1
            min_ops = min(min_ops, ops)

        # Check all lucky numbers with length len(n_str) - 1
        for bits in product(digits, repeat=len(n_str)-1):
            lucky = ''.join(bits)
            if lucky[0] == '0':
                continue
            ops = 0
            for i in range(len(n_str)-1):
                if n_str[i] != lucky[i]:
                    ops += 1
            min_ops = min(min_ops, ops)

        return min_ops

    for case in cases:
        print(min_ops(case))

if __name__ == '__main__':
    solve()