import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        # Find the smallest M such that M ^ (M + 1) == N
        # M ^ (M + 1) = (M | (M ^ (M + 1))) ^ (M + 1)
        # Let's find M by checking possible values
        found = False
        for M in range(1, 1 << 30):
            if (M ^ (M + 1)) == N:
                results.append(str(M))
                found = True
                break
        if not found:
            results.append("-1")
    print("\n".join(results))

if __name__ == '__main__':
    solve()