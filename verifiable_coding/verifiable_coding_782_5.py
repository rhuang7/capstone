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
        idx += 1
        costs = list(map(int, data[idx:idx+N]))
        idx += N
        W, Y = int(data[idx]), int(data[idx+1])
        idx += 2
        if Y > N:
            results.append("Not Possible")
            continue
        if W < Y:
            results.append("Not Possible")
            continue
        min_cost = 0
        for i in range(Y):
            min_cost += costs[i]
        results.append(str(min_cost))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()