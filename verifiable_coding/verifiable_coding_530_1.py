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
        # Minimum possible sum is N * m
        # Maximum possible sum is N * M
        if S < N * m or S > N * M:
            results.append("-1")
            continue
        
        # Try to find the lexicographically smallest proper sequence
        # We need to find a sequence where Fulu's program returns a value different from the correct median
        # Let's try to construct the lexicographically smallest sequence
        
        # Initialize the sequence with m's
        A = [m] * N
        
        # Try to adjust the sequence to make the sum S
        remaining = S - N * m
        # Distribute the remaining to the elements, trying to keep them as small as possible
        # Start from the end to keep the sequence lexicographically smallest
        for i in range(N-1, -1, -1):
            if remaining <= 0:
                break
            add = min(remaining, M - m)
            A[i] += add
            remaining -= add
        
        # Now check if this sequence is proper
        # Compute the correct median
        A_sorted = sorted(A)
        if N % 2 == 1:
            correct_median = A_sorted[N//2]
        else:
            correct_median = (A_sorted[N//2 - 1] + A_sorted[N//2]) / 2
        
        # Compute what Fulu's program would return
        # Find K such that 1 <= K <= N-1
        # The program removes A[K] and A[N mod K]
        # Then returns A[(N-2)//2]
        # We need to find a K that makes the result different from the correct median
        
        # Try all possible K values
        found = False
        for k in range(1, N):
            # Compute the indices to remove
            idx1 = k
            idx2 = N % k
            # Check if both indices are valid
            if idx1 >= N or idx2 >= N:
                continue
            # Remove the elements
            # We need to simulate the removal
            # But since the order is unchanged, we can just remove the elements
            # and then take the middle element
            # However, since we need to find a K that makes the result different
            # We can try to find such a K
            # Let's try to simulate the removal
            # We need to create a new array without the two elements
            # But since the original array is sorted, we can simulate the removal
            # by creating a new array without the two elements
            # However, since the order is unchanged, the two elements to remove
            # are at positions k and N % k in the original array
            # So we can simulate the removal by creating a new array
            # and then taking the middle element
            # But since the original array is sorted, the new array is also sorted
            # So the median is the middle element of the new array
            # But Fulu's program returns A[(N-2)//2] after the removal
            # So we need to find a K such that the value at (N-2)//2 is different from the correct median
            # Let's simulate the removal
            # Create a new array without the two elements
            new_A = []
            for i in range(N):
                if i == k or i == (N % k):
                    continue
                new_A.append(A[i])
            # Now compute the median of new_A
            if len(new_A) % 2 == 1:
                fulu_median = new_A[len(new_A)//2]
            else:
                fulu_median = (new_A[len(new_A)//2 - 1] + new_A[len(new_A)//2]) / 2
            # Compare with the correct median
            if fulu_median != correct_median:
                found = True
                break
        
        if found:
            results.append(' '.join(map(str, A)))
        else:
            results.append("-1")
    
    for res in results:
        print(res)