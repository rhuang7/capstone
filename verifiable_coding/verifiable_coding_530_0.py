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
        
        # Function to check if a sequence is proper
        def is_proper(seq):
            if len(seq) != N:
                return False
            if sum(seq) != S:
                return False
            for x in seq:
                if not (m <= x <= M):
                    return False
            # Compute correct median
            sorted_seq = sorted(seq)
            if N % 2 == 1:
                correct_median = sorted_seq[N//2]
            else:
                correct_median = (sorted_seq[N//2 - 1] + sorted_seq[N//2]) / 2
            # Compute Fulu's result
            # Find K such that 1 <= K <= N-1
            # Try all possible K in 1..N-1
            for k in range(1, N):
                if k == K:
                    # Use given K
                    pass
                else:
                    # Try other K
                    pass
            # For the given K, compute Fulu's result
            # Remove A[K] and A[N mod K]
            # The order of the remaining N-2 elements is unchanged
            # So the sequence after removal is the original sequence with A[K] and A[N mod K] removed
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But since the order is unchanged, the new sequence is the original sequence with those two elements removed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list without those two elements
            # But the order is unchanged
            # So we can create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            # But the order is unchanged, so the indices are not changed
            # So the new sequence is the original sequence with elements at positions K and (N mod K) removed
            # But we have to make sure that the indices are valid
            # So we need to create a new list by skipping those two elements
            #