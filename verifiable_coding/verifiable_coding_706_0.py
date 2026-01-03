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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        W = list(map(int, data[idx:idx+N]))
        idx += N
        total = sum(W)
        if total > K * 1000:
            results.append(-1)
            continue
        trips = 0
        i = 0
        while i < N:
            current_weight = 0
            j = i
            while j < N and current_weight + W[j] <= K:
                current_weight += W[j]
                j += 1
            if current_weight == 0:
                results.append(-1)
                break
            trips += 1
            i = j
        else:
            results.append(trips)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()