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
        
        # Check if it's possible to have a proper sequence
        # Minimum sum is N*m, maximum sum is N*M
        if S < N * m or S > N * M:
            results.append("-1")
            continue
        
        # Try to construct the lexicographically smallest sequence
        # Start with all m's
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Distribute the remaining to make the sequence lexicographically smallest
        # We want to increase the elements from left to right as little as possible
        # But we need to ensure that Fulu's program returns a different value than the correct median
        
        # Function to compute the correct median
        def correct_median(A):
            A_sorted = sorted(A)
            if N % 2 == 1:
                return A_sorted[N//2]
            else:
                return (A_sorted[N//2 - 1] + A_sorted[N//2]) / 2
        
        # Function to compute Fulu's program result
        def fulu_median(A, K):
            A_sorted = sorted(A)
            # Find K and N mod K
            k = K
            n_mod_k = N % k
            # Remove A[k] and A[n_mod_k]
            # Since the array is sorted, we can just remove those indices
            # But we need to make sure that the indices are valid
            if k >= len(A_sorted) or n_mod_k >= len(A_sorted):
                return -1
            # Remove the elements
            # To simulate removal, we can create a new list without those elements
            # But we need to preserve the order of the remaining elements
            # So we can create a new list that excludes those indices
            # However, since the original array is sorted, we can just remove the elements
            # and return the middle element
            # But since the original array is sorted, the new array is also sorted
            # So the median is the middle element of the new array
            # So we can just compute the median of the new array
            # But we need to make sure that the indices are valid
            if k >= len(A_sorted) or n_mod_k >= len(A_sorted):
                return -1
            # Remove the elements at indices k and n_mod_k
            # Since the array is sorted, we can just create a new array without those elements
            # But we need to make sure that the indices are valid
            # So we can create a new array with the elements not at those indices
            new_A = []
            for i in range(len(A_sorted)):
                if i != k and i != n_mod_k:
                    new_A.append(A_sorted[i])
            # The new array has N-2 elements
            # The median is the element at (N-2)//2
            if len(new_A) == 0:
                return -1
            return new_A[(N-2)//2]
        
        # Try to find the lexicographically smallest sequence
        # We will try to increase the elements from left to right
        # Start with all m's
        A = [m] * N
        total = N * m
        remaining = S - total
        
        # Try to distribute the remaining to make the sequence lexicographically smallest
        # But also ensure that Fulu's program returns a different value than the correct median
        found = False
        for i in range(N):
            # Try to increase A[i] as little as possible
            # The minimum increase is 1, but we need to make sure that the total is S
            # Also, we need to ensure that the sequence is valid
            # Try to increase A[i] by 1, if possible
            if A[i] < M:
                # Try to increase A[i] by 1
                A[i] += 1
                total += 1
                remaining -= 1
                if remaining == 0:
                    # Check if this sequence is a proper sequence
                    # Compute the correct median
                    correct = correct_median(A)
                    # Compute Fulu's median
                    fulu = fulu_median(A, K)
                    if fulu != correct:
                        found = True
                        break
                    else:
                        # Try to decrease A[i] back
                        A[i] -= 1
                        total -= 1
                        remaining += 1
                else:
                    # Check if this sequence is a proper sequence
                    correct = correct_median(A)
                    fulu = fulu_median(A, K)
                    if fulu != correct:
                        found = True
                        break
            else:
                # Can't increase A[i]
                pass
        
        if found:
            results.append(' '.join(map(str, A)))
        else:
            results.append("-1")
    
    for res in results:
        print(res)