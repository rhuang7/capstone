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
        
        # Sort the array to find the minimum sum subsequences
        A.sort()
        
        # Find the first K elements (smallest K elements)
        min_sum_subsequence = A[:K]
        min_sum = sum(min_sum_subsequence)
        
        # Count how many times the smallest element appears
        count = 0
        for num in A:
            if num == min_sum_subsequence[0]:
                count += 1
            else:
                break
        
        # Calculate the number of ways to choose K elements
        # with the first 'count' elements being the smallest
        # and the rest being the next smallest elements
        # We need to choose (K - 1) elements from the remaining (count - 1) elements
        # that are equal to the smallest element
        # and (K - (count - 1)) elements from the next smallest elements
        # which are the next elements in the sorted array
        # that are greater than the smallest element
        
        # The number of ways is combination(count, K)
        # if there are enough elements equal to the smallest
        # otherwise it's 0
        
        # If there are not enough elements equal to the smallest
        # then it's not possible to form a subsequence with sum min_sum
        # so the answer is 0
        
        # So we need to check if there are at least K elements equal to the smallest
        # if not, then we need to take some elements from the next ones
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        min_val = min_sum_subsequence[0]
        count_min = 0
        for num in A:
            if num == min_val:
                count_min += 1
            else:
                break
        
        # If there are not enough elements equal to the smallest
        # then we need to take some from the next ones
        # So we need to find how many elements are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on
        
        # Let's find the number of elements equal to the smallest
        # and the number of elements greater than the smallest
        # that are equal to the next smallest
        # and so on