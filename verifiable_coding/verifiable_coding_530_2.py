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
        # Minimum sum is N * m, maximum sum is N * M
        if S < N * m or S > N * M:
            results.append("-1")
            continue
        
        # Try to find the lex smallest proper sequence
        # We'll try to make the sequence as lex small as possible
        # Start with all elements as m, then adjust to meet sum S
        # Also need to ensure that Fulu's program returns a value different from the correct median
        
        # Lex smallest sequence is [m, m, ..., m]
        # Let's try to find the smallest possible sequence that is proper
        
        # First, try to make the sequence as lex small as possible
        # Start with all elements as m, then increase some elements to reach sum S
        # We'll try to make the sequence as small as possible, but ensure that Fulu's program returns a different value than the correct median
        
        # We'll try to generate the lex smallest sequence that is proper
        # We'll try to make the sequence as small as possible, but ensure that Fulu's program returns a different value than the correct median
        
        # Generate the lex smallest sequence
        A = [m] * N
        remaining = S - N * m
        # We need to distribute the remaining to make the sequence as small as possible
        # We'll increase the elements starting from the end to keep the sequence lex smallest
        
        for i in range(N-1, -1, -1):
            if remaining <= 0:
                break
            # We can increase A[i] up to M
            max_increase = min(remaining, M - A[i])
            A[i] += max_increase
            remaining -= max_increase
        
        # Now check if this sequence is proper
        # Compute the correct median
        A_sorted = sorted(A)
        if N % 2 == 1:
            correct_median = A_sorted[N//2]
        else:
            correct_median = (A_sorted[N//2 - 1] + A_sorted[N//2]) / 2
        
        # Now simulate Fulu's program
        # Find K (given), and remove A[K] and A[N % K]
        # Note: K is given, so we don't need to choose it
        # But the problem says that Fulu can choose K arbitrarily, so we need to find a K that makes the program return a different value
        
        # We need to find a K in [1, N-1] such that the program returns a different value than the correct median
        
        # Try all K in [1, N-1]
        found = False
        for K_candidate in range(1, N):
            # Remove A[K_candidate] and A[N % K_candidate]
            # Note: the order of the remaining elements is unchanged
            # So we need to remove the two elements and then take the middle element
            
            # Find the indices to remove
            # K_candidate is the index to remove
            # N % K_candidate is the other index to remove
            # But we need to make sure that the two indices are different and valid
            # Also, the indices must be in the range [0, N-1]
            
            # Get the two indices to remove
            idx1 = K_candidate
            idx2 = N % K_candidate
            if idx1 == idx2:
                continue  # skip if the same index
            
            # Check if the indices are valid
            if idx1 >= N or idx2 >= N:
                continue
            
            # Create a copy of the array
            A_copy = A[:]
            # Remove the elements at idx1 and idx2
            # We need to remove them in a way that the order of the remaining elements is unchanged
            # So we need to remove the elements in a way that the order is preserved
            # We'll create a new list that excludes the two indices
            
            # Create a new list that excludes the two indices
            new_A = []
            for i in range(N):
                if i != idx1 and i != idx2:
                    new_A.append(A_copy[i])
            
            # Now, the new array has length N-2
            # The program returns the element at (N-2)//2
            # So we need to check if this value is different from the correct median
            
            # Compute the value returned by Fulu's program
            if len(new_A) % 2 == 1:
                fulu_value = new_A[(len(new_A)-1)//2]
            else:
                fulu_value = (new_A[len(new_A)//2 - 1] + new_A[len(new_A)//2]) / 2
            
            # Check if fulu_value is different from correct_median
            if fulu_value != correct_median:
                found = True
                break
        
        if found:
            results.append(' '.join(map(str, A)))
        else:
            results.append("-1")
    
    for res in results:
        print(res)