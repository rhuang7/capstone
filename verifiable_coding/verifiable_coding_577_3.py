import sys

def solve():
    S = sys.stdin.buffer.read().split()[0].decode()
    N = int(sys.stdin.buffer.read().split()[0].decode())
    for _ in range(N):
        word = sys.stdin.buffer.read().strip().decode()
        can_read = all(c in S for c in word)
        print("Yes" if can_read else "No")

if __name__ == '__main__':
    solve()