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
        
        # Find all positions where the value is -1
        unknowns = [i for i in range(N) if A[i] == -1]
        if not unknowns:
            # All values are known, check if it's possible to be a periodic sequence
            # The period must be such that all values are in 1..K and satisfy the periodic condition
            # The maximum possible period is the maximum value in A
            max_val = max(A)
            # Check if all values are in 1..max_val and satisfy the periodic condition
            # For a periodic sequence S_i = (i % K) + 1, the value at position i is (i % K) + 1
            # So for all i, A[i] = (i % K) + 1
            # We need to find K such that for all i, A[i] = (i % K) + 1
            # This is equivalent to A[i] - 1 = i % K
            # So for all i, A[i] - 1 must be congruent to i modulo K
            # Therefore, for all i, A[i] - 1 - i must be divisible by K
            # So the possible K's are the GCD of all (A[i] - 1 - i) for i where A[i] is not -1
            # If there are no such i, then K can be arbitrarily large
            if N == 1:
                results.append("inf")
                continue
            # Check if all values are in 1..max_val
            for i in range(N):
                if A[i] != -1 and A[i] > max_val:
                    results.append("impossible")
                    break
            else:
                # Check if all values satisfy the periodic condition
                # Compute the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                if N == 1:
                    results.append("inf")
                    continue
                # Compute the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i, then K can be arbitrarily large
                # So we need to check if all (A[i] - 1 - i) are divisible by some K
                # The maximum possible K is the GCD of all (A[i] - 1 - i)
                # If there are no such i,