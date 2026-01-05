import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, P, Q = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to find the maximum number of creatures that can be paid back
        # Each creature requires exactly Ai rupees, and we have P one-rupee coins and Q two-rupee coins
        # So for each creature, the total amount needed is Ai
        # We need to find the maximum subset of A where the sum of Ai's is <= P + 2*Q
        
        # Sort A to try to select the smallest possible Ai's first
        A.sort()
        
        # We can use a greedy approach: try to select as many small Ai's as possible
        # We can use a binary search approach to find the maximum number of creatures that can be paid back
        
        # We can use a prefix sum array
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + A[i]
        
        # Now we need to find the maximum k such that prefix[k] <= P + 2*Q
        # But we also need to ensure that the number of one-rupee coins is sufficient
        # For each creature, the amount is Ai, and we can use 1-rupee coins and 2-rupee coins
        # So for each Ai, we can use min(Ai, P) one-rupee coins and the rest can be covered by two-rupee coins
        # But this is not straightforward, so we need a better approach
        
        # We can use a binary search approach on k
        # For each k, we can check if it's possible to select k creatures such that the total amount is <= P + 2*Q
        # And also, the number of one-rupee coins is sufficient
        # We can use a greedy approach to select the k smallest Ai's and check if it's possible
        
        # Binary search for the maximum k
        low = 0
        high = N
        best = 0
        while low <= high:
            mid = (low + high) // 2
            # Check if it's possible to select mid creatures
            # We take the first mid elements (smallest ones)
            # We need to check if the sum of these mid elements is <= P + 2*Q
            # And also, the number of one-rupee coins is sufficient
            # We can use a greedy approach to distribute the coins
            # For each Ai in the first mid elements, we can use as many 2-rupee coins as possible
            # The remaining amount is covered by 1-rupee coins
            # So the total 1-rupee coins needed is sum( (Ai % 2) for Ai in first mid elements )
            # And the total 2-rupee coins needed is sum( Ai // 2 for Ai in first mid elements )
            # We need to check if these are <= P and Q respectively
            if mid == 0:
                best = 0
                low = mid + 1
                continue
            total = prefix[mid]
            if total > P + 2 * Q:
                high = mid - 1
            else:
                # Check if the 1-rupee coins are sufficient
                ones_needed = 0
                twos_needed = 0
                for i in range(mid):
                    ai = A[i]
                    ones_needed += ai % 2
                    twos_needed += ai // 2
                if ones_needed <= P and twos_needed <= Q:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1
        results.append(str(best))
    print('\n'.join(results))