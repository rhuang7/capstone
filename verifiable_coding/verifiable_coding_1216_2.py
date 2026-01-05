import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, X = int(input[idx]), int(input[idx+1])
        idx += 2
        A = list(map(int, input[idx:idx+N]))
        idx += N
        if any(a >= X for a in A):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()