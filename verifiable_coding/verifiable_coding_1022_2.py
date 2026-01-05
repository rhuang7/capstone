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
        # So the number of cities must be even
        # Also, for each pair of opposite cities, the sum of the roads between them must be even
        # Because the clockwise and counterclockwise distances must be equal
        
        # We can pair cities as (1, N/2 + 1), (2, N/2 + 2), etc.
        # For each pair, the sum of the roads between them must be even
        # So for each pair (i, j), A[i-1] + A[j-1] must be even
        
        # Check if it's possible to assign values to -1 entries such that all pairs have even sum
        # We can try to assign values to -1 entries in a way that makes all pairs have even sum
        
        # Create a list of pairs
        pairs = []
        for i in range(N // 2):
            pairs.append((i + 1, N - i))
        
        # Try to assign values to -1 entries
        # We can assign 1 to all -1 entries
        # But we need to check if it's possible to make all pairs have even sum
        # If not, we can try to flip some values
        
        # Try to assign 1 to all -1 entries
        # Check if it's possible
        valid = True
        for i in range(N // 2):
            a = A[i - 1] if A[i - 1] != -1 else 1
            b = A[N - i - 1] if A[N - i - 1] != -1 else 1
            if (a + b) % 2 != 0:
                valid = False
                break
        
        if valid:
            # Check if all values are positive
            for val in A:
                if val == -1:
                    # We assigned 1, which is positive
                    pass
                else:
                    if val <= 0:
                        valid = False
                        break
            if valid:
                results.append("YES")
                results.append(' '.join(map(str, A)))
                continue
        
        # If not valid, try to flip some values
        # We can try to flip the value of one of the -1 entries in each pair
        # Try to flip one of the -1 entries in each pair
        # Try to assign 1 to one and 2 to the other
        # Check if it's possible
        
        # Try to flip one of the -1 entries in each pair
        # We can try to flip the first -1 entry in each pair
        # If that doesn't work, try to flip the second -1 entry
        # We can try to assign 1 to one and 2 to the other
        # If that doesn't work, then it's impossible
        
        # Try to assign 1 to one and 2 to the other in each pair
        # Check if it's possible
        valid = True
        for i in range(N // 2):
            a = A[i - 1] if A[i - 1] != -1 else 1
            b = A[N - i - 1] if A[N - i - 1] != -1 else 1
            if (a + b) % 2 != 0:
                # Try to flip one of them
                # Try to assign 1 to a and 2 to b
                a = 1
                b = 2
                if (a + b) % 2 != 0:
                    # Try to assign 2 to a and 1 to b
                    a = 2
                    b = 1
                    if (a + b) % 2 != 0:
                        valid = False
                        break
        
        if valid:
            # Check if all values are positive
            for val in A:
                if val == -1:
                    # We assigned 1 or 2, which are positive
                    pass
                else:
                    if val <= 0:
                        valid = False
                        break
            if valid:
                results.append("YES")
                results.append(' '.join(map(str, A)))
                continue
        
        # If none of the above worked, it's impossible
        results.append("NO")
    
    print('\n'.join(results))