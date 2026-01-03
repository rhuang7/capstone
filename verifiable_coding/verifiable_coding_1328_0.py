import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def min_ops(n_str):
        n = int(n_str)
        min_ops = float('inf')

        # Check all possible lucky numbers with the same length as n
        for length in range(1, len(n_str)+1):
            for lucky in ['4', '7'] * (length // 2) + ['4', '7'] * (length % 2):
                lucky_num = int(''.join(lucky))
                if lucky_num < n:
                    ops = len(n_str) - len(str(lucky_num)) + (len(str(lucky_num)) - len(str(n)))
                    min_ops = min(min_ops, ops)
                else:
                    ops = len(n_str) - len(str(lucky_num)) + (len(str(lucky_num)) - len(str(n)))
                    min_ops = min(min_ops, ops)

        # Check all possible lucky numbers with length + 1
        for lucky in ['4', '7'] * (len(n_str) // 2) + ['4', '7'] * (len(n_str) % 2):
            lucky_num = int(''.join(lucky))
            ops = len(n_str) + 1 - len(str(lucky_num)) + (len(str(lucky_num)) - len(str(n)))
            min_ops = min(min_ops, ops)

        return min_ops

    for case in cases:
        print(min_ops(case))

if __name__ == '__main__':
    solve()