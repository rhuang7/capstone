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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        max_val = -float('inf')
        min_val = float('inf')
        for num in arr:
            max_val = max(max_val, num + K)
            min_val = min(min_val, num - K)
        results.append(str(max_val - min_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()