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
        if Y == 0:
            results.append("0")
            continue
        if W < Y:
            results.append("Not Possible")
            continue
        min_cost = sum(sorted(costs)[:Y]) * 1
        results.append(str(min_cost))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()