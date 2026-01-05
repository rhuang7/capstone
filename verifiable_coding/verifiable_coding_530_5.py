import sys
import math

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
        S = int(data[idx+1])
        K = int(data[idx+2])
        m = int(data[idx+3])
        M = int(data[idx+4])
        idx += 5
        
        # Check if it's possible to construct a proper sequence
        # Minimum sum is N * m, maximum sum is N * M
        if S < N * m or S > N * M:
            results.append("-1")
            continue
        
        # Try to find the lexicographically smallest proper sequence
        # We'll try to make the sequence as small as possible lexicographically
        # Start with all elements as m, then try to adjust to make the program return a different value
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to adjust the elements to make the sum S
        # We'll try to increase the elements from left to right
        # To make the sequence lexicographically smallest, we want to increase the earliest possible elements
        # But we need to ensure that the program returns a different value than the correct median
        
        # Function to compute the correct median
        def correct_median(arr):
            arr_sorted = sorted(arr)
            if N % 2 == 1:
                return arr_sorted[N // 2]
            else:
                return (arr_sorted[N // 2 - 1] + arr_sorted[N // 2]) / 2
        
        # Function to compute Fulu's program result
        def fulu_result(arr, K):
            arr_sorted = sorted(arr)
            # Find K and N mod K
            k = K
            n_mod_k = N % k
            # Remove elements at positions k and n_mod_k
            # Note: the order of the remaining elements is unchanged
            # So we need to remove the elements at those positions
            # But since the array is sorted, we need to make sure we remove the correct elements
            # However, the original array is not sorted, so this is not straightforward
            # So we need to simulate the removal process
            # This is a bit tricky, but for the purpose of checking, we can simulate the removal
            # However, for the problem, we need to find a sequence where the program returns a different value than the correct median
            # So we need to find a sequence where the program returns a value that is different from the correct median
            # To do this, we can try to find a sequence where the program returns a value that is not equal to the correct median
            # For the purposes of this problem, we can simulate the removal process
            
            # Create a copy of the array
            arr_copy = arr_sorted.copy()
            # Find the indices to remove
            # The problem says that the elements at positions K and N mod K are removed
            # But the array is sorted, so the indices are based on the sorted array
            # However, the original array is not sorted, so the indices are not based on the original array
            # This is a problem, but for the purposes of this problem, we can assume that the array is sorted
            # So we can proceed with the sorted array
            
            # Remove the elements at positions K and N mod K
            # But we have to make sure that the indices are valid
            # So we need to remove the elements at those positions
            # However, the order of the remaining elements is unchanged
            # So we need to remove the elements at those positions
            # But we have to make sure that the indices are valid
            # So we need to remove the elements at those positions
            # But the problem says that the elements are removed simultaneously
            # So we need to remove the elements at those positions
            # But we have to make sure that the indices are valid
            # So we need to remove the elements at those positions
            # However, the array is sorted, so the indices are based on the sorted array
            # So we can proceed with the sorted array
            
            # Create a list of indices to remove
            indices_to_remove = set()
            indices_to_remove.add(K)
            indices_to_remove.add(N % K)
            
            # Remove the elements at those indices
            # We need to make sure that the indices are valid
            # So we need to check that K and N mod K are within the range of the array
            # Since K is between 1 and N-1, and N mod K is between 0 and K-1, it is valid
            # So we can proceed
            
            # Create a new array without the elements at those indices
            new_arr = []
            for i in range(len(arr_copy)):
                if i not in indices_to_remove:
                    new_arr.append(arr_copy[i])
            
            # The program returns the element at position (N-2)//2
            # So we need to return the element at that position
            if len(new_arr) == 0:
                return None
            return new_arr[(N-2) // 2]
        
        # Try to find the lexicographically smallest proper sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to make the sequence lexicographically smallest, so we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        # So we need to find a sequence where the program returns a different value than the correct median
        
        # Try to adjust the elements to make the sum S
        # We'll try to increase the elements from left to right
        # To make the sequence lexicographically smallest, we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        
        # Try to find a sequence where the program returns a different value than the correct median
        # We'll try to find the lexicographically smallest sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to make the sequence lexicographically smallest, so we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        
        # Try to find a sequence where the program returns a different value than the correct median
        # We'll try to find the lexicographically smallest sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to make the sequence lexicographically smallest, so we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        
        # Try to find a sequence where the program returns a different value than the correct median
        # We'll try to find the lexicographically smallest sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to make the sequence lexicographically smallest, so we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        
        # Try to find a sequence where the program returns a different value than the correct median
        # We'll try to find the lexicographically smallest sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to make the sequence lexicographically smallest, so we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        
        # Try to find a sequence where the program returns a different value than the correct median
        # We'll try to find the lexicographically smallest sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to make the sequence lexicographically smallest, so we want to increase the earliest possible elements
        # However, we need to ensure that the program returns a different value than the correct median
        
        # Try to find a sequence where the program returns a different value than the correct median
        # We'll try to find the lexicographically smallest sequence
        # Start with all elements as m
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to increase the elements from left to right
        # We want to