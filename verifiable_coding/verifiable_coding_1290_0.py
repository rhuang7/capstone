import sys

def solve():
    N = sys.stdin.buffer.read().strip()
    if N == b'0':
        print("1")
        return
    N = int(N)
    if 0 <= N < 10:
        print("1")
    elif 10 <= N < 100:
        print("2")
    elif 100 <= N < 1000:
        print("3")
    else:
        print("More than 3 digits")

if __name__ == '__main__':
    solve()