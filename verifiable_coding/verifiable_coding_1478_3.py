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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Replace -1 with possible values
        # We need to find the maximum possible K such that A is a contiguous subsequence of some periodic sequence
        # The periodic sequence S_i = (i % K) + 1
        
        # First, check if all elements are -1
        if all(x == -1 for x in A):
            results.append("inf")
            continue
        
        # Find all possible positions where -1 occurs
        pos = [i for i in range(N) if A[i] == -1]
        
        # Try to fill in the -1s with values that make the sequence periodic
        # For each possible K, check if the sequence can be made periodic
        # The maximum possible K is N, since if K >= N, the sequence can be arbitrary
        # So we try K from N down to 1, and check if it's possible
        # If we find a K that works, that's the maximum possible
        # If no K works, output "impossible"
        
        # First, check if K can be arbitrarily large
        # For K to be arbitrarily large, all elements must be unique in the sequence
        # So check if all elements are unique and there are no -1s
        if all(x != -1 for x in A) and len(set(A)) == N:
            results.append("inf")
            continue
        
        # Try K from N down to 1
        max_k = -1
        for K in range(N, 0, -1):
            # Check if the sequence can be made periodic with period K
            # For each position i in the sequence, the value should be (i % K) + 1
            # But we have to fill in the -1s with possible values
            # So for each position i, if A[i] is not -1, it must be equal to (i % K) + 1
            # If it is -1, we can fill it with any value that is (i % K) + 1
            # So for each position i, if A[i] is not -1, it must be equal to (i % K) + 1
            valid = True
            for i in range(N):
                if A[i] != -1:
                    if (i % K) + 1 != A[i]:
                        valid = False
                        break
            if valid:
                max_k = K
                break
        
        if max_k != -1:
            results.append(str(max_k))
        else:
            results.append("impossible")
    
    print('\n'.join(results))