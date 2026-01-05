import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N1 = int(input[idx])
        N2 = int(input[idx+1])
        N3 = int(input[idx+2])
        idx += 3
        # Total triples without restriction: N1 * N2 * N3
        total = (N1 * N2) % MOD
        total = (total * N3) % MOD
        # Subtract cases where at least two numbers are equal
        # Case 1: X1 == X2
        case1 = (N1 * N2) % MOD
        case1 = (case1 * N3) % MOD
        # Case 2: X1 == X3
        case2 = (N1 * N3) % MOD
        case2 = (case2 * N2) % MOD
        # Case 3: X2 == X3
        case3 = (N2 * N3) % MOD
        case3 = (case3 * N1) % MOD
        # Add back cases where all three are equal (subtracted twice)
        case_all = (N1 * N2 * N3) % MOD
        # Apply inclusion-exclusion principle
        res = (total - case1 - case2 - case3 + case_all) % MOD
        # Ensure non-negative result
        if res < 0:
            res += MOD
        print(res)

if __name__ == '__main__':
    solve()