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
        # Since the impacts are at distinct integral points, we can choose any set of points
        # We need to check if there exists a set of N distinct integers such that the sum of K^|Xi - X0| equals M
        
        # The minimal possible sum is when all impacts are at the same point (but they must be distinct, so we need to choose points close to X0)
        # The maximum possible sum is unbounded, but since M is up to 1e18, we need to check if M can be formed with N terms
        
        # Let's consider the minimal possible sum when we choose N points closest to X0
        # We can choose points X0 - 1, X0 - 2, ..., X0 - N (or X0 + 1, X0 + 2, ..., X0 + N)
        # The sum would be K^1 + K^2 + ... + K^N
        
        # If K == 1, then the sum is N, so we need M == N
        if K == 1:
            if M == N:
                results.append("yes")
            else:
                results.append("no")
            continue
        
        # For K > 1, the sum of K^1 + K^2 + ... + K^N is a geometric series
        # The sum is (K^(N+1) - K) / (K - 1)
        # We need to check if M is greater than or equal to this sum
        # Also, since we can choose any N distinct points, we can make the sum as large as needed
        
        # Check if M is at least the minimal sum
        # The minimal sum is when we choose N points closest to X0
        # The sum is K^1 + K^2 + ... + K^N
        # We can compute this sum and check if M is at least that
        
        # Compute the minimal sum
        minimal_sum = 0
        for i in range(1, N+1):
            minimal_sum += K ** i
        
        if M >= minimal_sum:
            results.append("yes")
        else:
            results.append("no")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()