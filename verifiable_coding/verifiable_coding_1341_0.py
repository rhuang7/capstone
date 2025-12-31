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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute the number of valid contiguous subsequences
        # that when removed leave a strictly increasing sequence
        # We'll use a greedy approach to find the longest increasing subsequence
        # and count the valid removals based on that
        
        # Find the length of the longest strictly increasing subsequence
        # This is done in O(N) time using a greedy approach
        l = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                l += 1
            else:
                l = 1
        # The number of valid removals is (total possible contiguous subsequences) - (number of invalid ones)
        # Total possible contiguous subsequences is N*(N+1)//2
        # Invalid ones are those that are not strictly increasing
        # But we can't directly subtract, so we use the length of the LIS
        # The number of valid removals is (N - l) * (N - l + 1) // 2
        # Because we can remove any contiguous subsequence of length (N - l) or less
        # that is not part of the LIS
        # However, this is not accurate, so we need to find all valid contiguous subsequences
        # that when removed leave a strictly increasing sequence
        
        # Correct approach: For each position, find the longest increasing run
        # and count the number of valid removals based on that
        
        # We'll use a dynamic programming approach
        # dp[i] = length of the longest increasing subsequence ending at i
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Now, for each i, the number of valid removals is dp[i] - 1
        # Because we can remove any subsequence of length 1 to dp[i] - 1
        # that ends at i
        total = 0
        for i in range(N):
            total += dp[i] - 1
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()