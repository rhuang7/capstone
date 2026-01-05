import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = data[i]
        digits = list(N)
        digits.sort(reverse=True)
        X = ''.join(digits)
        results.append(X)
    print('\n'.join(results))

if __name__ == '__main__':
    solve()