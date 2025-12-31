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
        # Since all Xi are distinct, we need to find if there exists a set of N distinct integers such that the sum is M
        
        # The minimal possible sum is when all Xi are as close as possible to X0
        # The minimal sum is when Xi are X0 - 1, X0 - 2, ..., X0 - N (or X0 + 1, ..., X0 + N)
        # The minimal sum is the sum of K^1 + K^2 + ... + K^N
        # The maximal possible sum is unbounded, but since M is up to 1e18, we can check if M is at least the minimal sum
        
        # Compute the minimal sum
        min_sum = 0
        for i in range(1, N+1):
            min_sum += K ** i
        
        if min_sum > M:
            results.append("no")
        else:
            results.append("yes")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()