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
        # So N must be even
        # Also, for each pair of opposite cities, the sum of their roads must be even
        # Because the clockwise and counter-clockwise distances must be equal
        
        # Create a list of pairs of opposite cities
        pairs = []
        for i in range(N // 2):
            pairs.append((i, i + N // 2))
        
        # For each pair, check if the sum of their roads is even
        # If any pair has both roads unknown, we can set them to 1
        # If one is known and the other is unknown, we set the unknown to (even - known)
        # If both are known, check if their sum is even
        valid = True
        for i, j in pairs:
            a = A[i]
            b = A[j]
            if a == -1 and b == -1:
                A[i] = 1
                A[j] = 1
            elif a == -1:
                A[i] = (1 - b) if (1 - b) > 0 else 1
            elif b == -1:
                A[j] = (1 - a) if (1 - a) > 0 else 1
            else:
                if (a + b) % 2 != 0:
                    valid = False
                    break
        
        if not valid:
            results.append("NO")
            continue
        
        # Check if all roads are positive
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