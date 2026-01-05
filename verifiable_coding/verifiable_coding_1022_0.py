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
        
        # Check if N is even or odd
        if N % 2 != 0:
            results.append("NO")
            continue
        
        # For each city, there must be an opposite city
        # So for each i, there must be a j such that the clockwise and counterclockwise distances are equal
        # This is only possible if N is even and each city has a unique opposite
        # So we can pair cities as (i, i + N//2) for i in 0 to N//2 - 1
        
        # Create a list of pairs
        pairs = []
        for i in range(N // 2):
            pairs.append((i, i + N // 2))
        
        # Check if the given A has valid values for the pairs
        # For each pair, if both are -1, we can assign the same value
        # If one is known and the other is -1, we set the other to the known value
        # If both are known, they must be equal
        valid = True
        for i, j in pairs:
            a = A[i]
            b = A[j]
            if a == -1 and b == -1:
                # Both unknown, assign same value
                pass
            elif a == -1:
                # Set b to a
                A[j] = a
                valid = False
            elif b == -1:
                # Set a to b
                A[i] = b
                valid = False
            else:
                # Both known, must be equal
                if a != b:
                    valid = False
                    break
        
        if not valid:
            results.append("NO")
            continue
        
        # Now check if all roads are positive
        for a in A:
            if a <= 0:
                valid = False
                break
        
        if not valid:
            results.append("NO")
            continue
        
        results.append("YES")
        results.append(' '.join(map(str, A)))
    
    print('\n'.join(results))