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
        H = list(map(int, data[idx:idx+N]))
        idx += N
        H.sort(reverse=True)
        min_boxes = float('inf')
        # Check all possible splits of the top boxes
        for i in range(1, N):
            # First tower is sum of first i boxes
            # Second tower is sum of remaining boxes
            sum1 = sum(H[:i])
            sum2 = sum(H[i:])
            if sum1 >= K and sum2 >= K:
                min_boxes = min(min_boxes, i + (N - i))
        # Check if it's possible to form two towers
        if min_boxes != float('inf'):
            results.append(str(min_boxes))
        else:
            results.append('-1')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()