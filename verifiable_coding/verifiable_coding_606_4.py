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
        K = int(data[idx+1])
        M = int(data[idx+2])
        X0 = int(data[idx+3])
        idx += 4
        # The total impact is sum of K^|Xi - X0| for all impacts
        # Since all impacts are at distinct integral points, we can choose any distinct points
        # To maximize the total impact, we can choose points as far as possible from X0
        # But since we need to reach exactly M, we need to check if M can be formed by sum of K^d for some d >= 0
        # We can try all possible combinations of exponents
        # However, since K can be large, we need to find a way to check if M can be formed
        # We can try all possible combinations of exponents up to some limit
        # We can use a BFS approach to find if M can be formed
        # We can also use dynamic programming
        # Let's try a BFS approach
        from collections import deque
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add(0)
        found = False
        while queue:
            total, count = queue.popleft()
            if total == M:
                found = True
                break
            if count == N:
                continue
            # Try adding a new impact at a point that is not already used
            # The distance can be any positive integer
            # We can try adding distance 1, 2, ... up to some limit
            # But since K can be large, we need to limit the distance
            # For example, if K is 1000, then K^d grows very quickly
            # So for K >= 2, we can limit the distance to 60, since 2^60 is about 1e18
            # For K=1, K^d is always 1, so we can only have N terms of 1, so M must be N
            if K == 1:
                if M == N:
                    found = True
                break
            # Try distances from 1 to 60
            for d in range(1, 61):
                val = K ** d
                if total + val > M:
                    continue
                if total + val not in visited:
                    visited.add(total + val)
                    queue.append((total + val, count + 1))
        results.append("yes" if found else "no")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()