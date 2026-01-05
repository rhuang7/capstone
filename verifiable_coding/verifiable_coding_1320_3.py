import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        if N % 3 == 0:
            print("B")
        else:
            print("A")

if __name__ == '__main__':
    solve()