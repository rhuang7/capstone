import sys

def solve():
    S = sys.stdin.buffer.read().split()[0].decode()
    N = int(sys.stdin.buffer.read().split()[0].decode())
    for _ in range(N):
        word = sys.stdin.buffer.readline().strip().decode()
        if all(c in S for c in word):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()