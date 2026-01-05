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
        
        total = 0
        prefix = 0
        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        
        for k in range(N):
            # Compute the prefix sum up to k-1 and suffix sum from k+1
            prefix_k = prefix_sum[k]
            suffix_k = prefix_sum[N] - prefix_sum[k + 1]
            
            # Find the number of ways to split the array with B_k = 0
            # We need to find the number of pairs (i, j) such that i < k < j and prefix_sum[i] = suffix_sum[j]
            # Also, i must be in [0, k-1], j must be in [k+1, N-1]
            
            # We can use a hash map to store the prefix sums up to k-1
            # And check how many times each prefix sum appears
            # Similarly, for the suffix sums from k+1
            # But for efficiency, we can precompute all possible prefix and suffix sums and use two pointers
            
            # We'll use two pointers approach for each k
            left = 0
            right = N - 1
            count = 0
            
            while left < k and right > k:
                if prefix_sum[left] == prefix_sum[right] - A[k]:
                    count += 1
                    left += 1
                    right -= 1
                elif prefix_sum[left] < prefix_sum[right] - A[k]:
                    left += 1
                else:
                    right -= 1
            
            total += count
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()