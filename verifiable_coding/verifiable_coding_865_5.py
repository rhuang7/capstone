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
            # Because there are 2^(N-1) permutations that are not strictly increasing or decreasing
            # Subtract 2 to exclude the strictly increasing and strictly decreasing permutations
            # But for N >= 3, the strictly increasing and decreasing permutations do not satisfy the condition
            # So the answer is 2^(N-1) - 2
            ans = (pow(2, N-1, MOD) - 2) % MOD
            print(ans)

if __name__ == '__main__':
    solve()