import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        count = 0
        for _ in range(N):
            S = int(data[idx])
            J = int(data[idx + 1])
            idx += 2
            if J - S > 5:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()