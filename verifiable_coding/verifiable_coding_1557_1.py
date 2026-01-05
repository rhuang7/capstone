import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        S = data[idx]
        idx += 1
        R = data[idx]
        idx += 1
        if S == R:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()