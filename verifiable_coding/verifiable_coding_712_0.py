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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        if all(x % 2 == 1 for x in A):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()