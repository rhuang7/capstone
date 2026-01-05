import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = data[i]
        total = 0
        for c in N:
            total += int(c)
        print(total)

if __name__ == '__main__':
    solve()