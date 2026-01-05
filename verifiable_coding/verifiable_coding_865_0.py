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
            # The answer is 2 * (N-1) choose (N-2) - 2
            # Which simplifies to 2*(N-1) - 2 = 2*(N-2)
            # But this is only true for N >= 3
            # However, the correct formula is 2*(N-1) - 2 = 2*(N-2)
            # But for N=3, it's 2, which matches the sample
            # So the correct formula is 2*(N-2)
            print((2 * (N - 2)) % MOD)

if __name__ == '__main__':
    solve()