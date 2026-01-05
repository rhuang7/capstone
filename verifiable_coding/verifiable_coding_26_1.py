import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        if (n == 1 and m % 2 == 1) or (m == 1 and n % 2 == 1):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()