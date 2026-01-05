import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        X = input[idx]
        K = int(input[idx+1])
        idx += 2
        A = list(map(int, input[idx:idx+K]))
        idx += K
        B = list(map(int, input[idx:idx+K]))
        idx += K
        X = int(X)
        M = X
        for a, b in zip(A, B):
            M = M * (a + b) // b
        Z = (M - X) / M * 100
        results.append(int(Z))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()