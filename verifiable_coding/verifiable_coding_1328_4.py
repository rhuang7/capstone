import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def min_ops(s):
        n = len(s)
        min_ops = float('inf')

        # Check all possible lucky numbers with the same length as s
        for i in range(n):
            for j in range(i, n):
                if (i == 0 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 0):
                    continue
                # Generate all lucky numbers with length n
                for lucky in ["4", "7"]:
                    # Generate all combinations of 4 and 7 of length n
                    from itertools import product
                    for digits in product("47", repeat=n):
                        # Check if the current lucky number is valid
                        if digits[0] == '0':
                            continue
                        # Count the number of changes needed
                        ops = 0
                        for a, b in zip(s, digits):
                            if a != b:
                                ops += 1
                        min_ops = min(min_ops, ops)

        # Check all possible lucky numbers with length n+1
        for lucky in ["4", "7"]:
            # Generate all combinations of 4 and 7 of length n+1
            from itertools import product
            for digits in product("47", repeat=n+1):
                # Check if the current lucky number is valid
                if digits[0] == '0':
                    continue
                # Count the number of changes needed
                ops = 0
                for a, b in zip(s, digits):
                    if a != b:
                        ops += 1
                min_ops = min(min_ops, ops)

        return min_ops

    for case in cases:
        print(min_ops(case))

if __name__ == '__main__':
    solve()