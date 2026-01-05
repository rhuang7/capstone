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
        
        # Find the first K elements (they will form the minimum sum subsequence)
        min_subseq = A[:K]
        min_sum = sum(min_subseq)
        
        # Count how many times the smallest element appears
        count = 0
        for num in A:
            if num == min_subseq[-1]:
                count += 1
            else:
                break
        
        # If K is 1, the count is the number of occurrences of the smallest element
        if K == 1:
            results.append(count)
            continue
        
        # For K > 1, we need to count the number of ways to choose K elements
        # such that the first K elements are the smallest ones
        # We count how many times the smallest element appears, and then how many
        # times the next smallest element appears, etc.
        # But we need to ensure that we have exactly K elements
        
        # Count how many times each element in the min_subseq appears
        # in the original array
        from collections import defaultdict
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        
        # Calculate the number of ways to choose the elements
        from math import comb
        total = 1
        for i in range(K):
            total *= freq[min_subseq[i]]
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()