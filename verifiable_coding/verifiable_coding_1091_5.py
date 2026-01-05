import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        if N % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()