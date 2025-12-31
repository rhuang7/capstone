import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def min_ops(n_str):
        n = int(n_str)
        min_ops = float('inf')

        # Generate all possible lucky numbers with length equal to len(n_str)
        from itertools import product
        for bits in product([0, 1], repeat=len(n_str)):
            lucky = ''
            for b in bits:
                if b == 0:
                    lucky += '4'
                else:
                    lucky += '7'
            ops = 0
            for i in range(len(n_str)):
                if lucky[i] != n_str[i]:
                    ops += 1
            min_ops = min(min_ops, ops)

        # Check all possible lucky numbers with length len(n_str) + 1
        for bits in product([0, 1], repeat=len(n_str) + 1):
            lucky = ''
            for b in bits:
                if b == 0:
                    lucky += '4'
                else:
                    lucky += '7'
            ops = 0
            for i in range(len(n_str)):
                if lucky[i] != n_str[i]:
                    ops += 1
            min_ops = min(min_ops, ops)

        return min_ops

    for case in cases:
        print(min_ops(case))

if __name__ == '__main__':
    solve()