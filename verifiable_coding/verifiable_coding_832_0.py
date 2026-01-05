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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array to find the minimum sum subsequence
        A.sort()
        
        # The minimum sum subsequence is the first K elements
        min_sum = sum(A[:K])
        
        # Count how many times the smallest element appears
        count = 0
        for num in A:
            if num == A[0]:
                count += 1
            else:
                break
        
        # If K is 1, the answer is the count of the smallest element
        if K == 1:
            results.append(count)
            continue
        
        # Otherwise, count the number of ways to choose K elements
        # with the first (K - 1) elements being the smallest ones
        # and the last element being the next smallest
        # We need to find how many times the (K-th) smallest element appears
        # after the first (K - 1) smallest elements
        
        # Find the number of occurrences of the K-th smallest element
        # after the first (K - 1) smallest elements
        count_k = 0
        for i in range(K, N):
            if A[i] == A[K-1]:
                count_k += 1
            else:
                break
        
        # The number of interesting subsequences is count * count_k
        results.append(count * count_k)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()