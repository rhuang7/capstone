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
        # Since all Xi are distinct, we can choose any set of distinct integers
        # to maximize the sum. To achieve M, we need to find if there exists a set
        # of N distinct integers such that the sum of K^|Xi - X0| equals M.
        
        # The maximum possible sum for N impacts is when we choose the N largest
        # possible values of K^|Xi - X0|. Since K >= 1, the largest values are
        # when Xi is as far as possible from X0. However, since Xi must be distinct,
        # we can choose Xi as X0 + 1, X0 + 2, ..., X0 + N, or X0 - 1, X0 - 2, ..., X0 - N.
        
        # Let's try to find the maximum possible sum for N impacts.
        # We can choose the N largest possible values of K^|Xi - X0| by placing
        # the impacts as far as possible from X0.
        
        # Let's try to find the maximum sum for N impacts.
        # The maximum sum is when we place the impacts at positions X0 + 1, X0 + 2, ..., X0 + N
        # or X0 - 1, X0 - 2, ..., X0 - N. The sum of K^|Xi - X0| for these positions is:
        # sum_{i=1 to N} K^i
        
        # We can compute this sum and check if it is >= M.
        # If the maximum possible sum is less than M, then it is not possible.
        # If the maximum possible sum is >= M, then it is possible.
        
        # Compute the maximum possible sum for N impacts.
        max_sum = 0
        for i in range(1, N+1):
            max_sum += K ** i
        
        if max_sum >= M:
            results.append("yes")
        else:
            results.append("no")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()