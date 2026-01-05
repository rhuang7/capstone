import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    for i in range(1, t + 1):
        n = int(data[i])
        if n % 4 == 0 or n % 12 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()