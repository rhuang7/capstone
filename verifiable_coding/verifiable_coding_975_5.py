import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        R = int(data[idx+1])
        X_size = int(data[idx+2])
        Y_size = int(data[idx+3])
        idx +=4
        X = set()
        if X_size > 0:
            X = set(map(int, data[idx:idx+X_size]))
            idx += X_size
        Y = set()
        if Y_size > 0:
            Y = set(map(int, data[idx:idx+Y_size]))
            idx += Y_size
        eligible = 0
        for i in range(1, N+1):
            if i not in X and i not in Y:
                eligible += 1
        results.append(min(eligible, R))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()