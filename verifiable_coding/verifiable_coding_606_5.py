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
        
        # The total impact is the sum of K^|Xi - X0| for all impacts
        # Since the impacts are at distinct integral points, we can choose any set of distinct integers
        # We need to check if there exists a set of N distinct integers such that the sum of K^|Xi - X0| equals M
        
        # The minimal possible sum is when the impacts are at X0 - 1, X0 - 2, ..., X0 - N (or X0 + 1, X0 + 2, ..., X0 + N)
        # The minimal sum is sum_{i=1 to N} K^i
        # The maximal possible sum is unbounded, but we can check if M is at least the minimal sum and if M can be formed by adding powers of K
        
        # Compute minimal sum
        min_sum = 0
        for i in range(1, N+1):
            min_sum += K ** i
        
        if M < min_sum:
            results.append("no")
            continue
        
        # Check if M can be formed by adding powers of K
        # We can use a set to track the possible sums
        # We can use BFS to explore possible sums
        # We can also use a dynamic programming approach
        
        # Use BFS
        from collections import deque
        
        visited = set()
        queue = deque()
        queue.append(0)
        visited.add(0)
        
        while queue:
            current = queue.popleft()
            if current == M:
                results.append("yes")
                break
            if current > M:
                continue
            for i in range(1, N+1):
                next_val = current + K ** i
                if next_val not in visited and next_val <= M:
                    visited.add(next_val)
                    queue.append(next_val)
        else:
            results.append("no")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()