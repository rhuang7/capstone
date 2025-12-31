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
            # Because we need to count permutations with exactly one peak
            # and subtract the cases where the peak is at the ends
            ans = (pow(2, N-1, MOD) - 2) % MOD
            print(ans)

if __name__ == '__main__':
    solve()