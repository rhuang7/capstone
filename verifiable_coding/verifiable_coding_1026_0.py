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
        total = N1 * N2 * N3
        same = 0
        if N1 >= N2:
            same += N1 * N2 * (N1 - N2)
        if N1 >= N3:
            same += N1 * N3 * (N1 - N3)
        if N2 >= N3:
            same += N2 * N3 * (N2 - N3)
        ans = (total - same) % MOD
        print(ans)

if __name__ == '__main__':
    solve()