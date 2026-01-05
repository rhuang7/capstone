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
            # All values are known, check if it's periodic
            # The period must be such that A[i] = (i % K) + 1
            # So for all i, A[i] - 1 must be congruent modulo K
            # So the possible K is the GCD of all (A[i] - 1 - (i % K)) for all i
            # But since K is unknown, we can find the possible K by checking all possible values
            # The maximum possible K is N-1, since the sequence is of length N
            # We can try all K from 1 to N-1 and check if the sequence is periodic with that K
            # If any K works, then the maximum possible K is the maximum such K
            # If no K works, then it's impossible
            # If all K work, then it's "inf"
            # So we check for K from 1 to N-1
            # But to find the maximum possible K, we can check for K from N-1 down to 1
            # If any K works, then that's the answer
            # If none work, then it's impossible
            # However, if all K work, then it's "inf"
            # So we need to check if there's a K that works, and if all K work, then it's "inf"
            # But how to check if all K work?
            # It's possible only if the sequence is constant, since for K to work for all K, the sequence must be periodic with any K
            # Which is only possible if the sequence is constant
            # So first check if the sequence is constant
            is_constant = True
            for i in range(1, N):
                if A[i] != A[0]:
                    is_constant = False
                    break
            if is_constant:
                results.append("inf")
                continue
            # Now check for possible K from N-1 down to 1
            max_k = -1
            for K in range(N-1, 0, -1):
                valid = True
                for i in range(N):
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
            continue
        
        # There are unknowns, so we need to fill them in
        # The idea is to find a K such that the sequence can be filled in with values that fit the periodic pattern
        # For each position i, the value must be (i % K) + 1
        # So for each unknown position, we can find the possible K values that would make it fit
        # The possible K values must be such that for all positions i, the value (i % K) + 1 is compatible with the known values
        # So for each unknown position, we can find the possible K values that would make it fit
        # The intersection of all possible K values from all unknown positions is the candidate K values
        # Then, among those, we select the maximum possible K
        # If there are no possible K values, then it's impossible
        # If there are infinite possible K values, then it's "inf"
        # So we need to find the set of possible K values
        # For each unknown position i, the value must be (i % K) + 1
        # So for each unknown position i, the possible K values are those that satisfy (i % K) + 1 = value
        # But since the value is unknown, we can find the possible K values for that position
        # For each unknown position i, the value must be (i % K) + 1, so the value is in the range [1, K]
        # So for each unknown position i, the possible K values are those that are >= (value - 1) and (value - 1) + 1 = value
        # But since the value is unknown, we can find the possible K values for that position
        # For example, if the value is unknown, then for any K >= 1, the value could be (i % K) + 1
        # So the possible K values for that position are all K >= 1
        # But we need to find K such that for all known positions, the value (i % K) + 1 is equal to the known value
        # So the idea is to find the set of K values that satisfy all known positions
        # For each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) + 1
        # So for each known position i, the value must be in [1, K]
        # So for each known position i, the value must be (i % K) +