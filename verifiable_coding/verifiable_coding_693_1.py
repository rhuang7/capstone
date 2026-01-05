import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        fact = 1
        for j in range(1, N + 1):
            fact *= j
        results.append(str(fact))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()