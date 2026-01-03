import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        if N < 3:
            print(0)
        else:
            # The answer is 2^(N-1) - 2
            # Because we need to count permutations that have exactly one peak
            # And the number of such permutations is 2^(N-1) - 2
            # But for N >= 3, the answer is 2^(N-1) - 2
            # However, for N=3, 2^(3-1) - 2 = 4 - 2 = 2 which matches the example
            # So the formula is correct
            ans = pow(2, N-1, MOD) - 2
            print(ans % MOD)

if __name__ == '__main__':
    solve()