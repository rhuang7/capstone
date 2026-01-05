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
        
        if N % 2 != 0:
            results.append("NO")
            continue
        
        opposite = [0] * N
        for i in range(N):
            j = (i + N // 2) % N
            opposite[i] = j
        
        # Check if opposite cities are correctly paired
        for i in range(N):
            j = opposite[i]
            if i < j:
                if A[i] == -1 or A[j] == -1:
                    results.append("NO")
                    break
            else:
                if A[j] == -1 or A[i] == -1:
                    results.append("NO")
                    break
        else:
            # Try to assign values to unknown roads
            # For each pair of opposite cities, assign the same value
            # If one is known, set the other to the same value
            # If both are unknown, set them to 1
            new_A = A[:]
            for i in range(N):
                j = opposite[i]
                if i < j:
                    if new_A[i] == -1 and new_A[j] == -1:
                        new_A[i] = 1
                        new_A[j] = 1
                    elif new_A[i] == -1:
                        new_A[i] = new_A[j]
                    elif new_A[j] == -1:
                        new_A[j] = new_A[i]
                else:
                    if new_A[j] == -1 and new_A[i] == -1:
                        new_A[j] = 1
                        new_A[i] = 1
                    elif new_A[j] == -1:
                        new_A[j] = new_A[i]
                    elif new_A[i] == -1:
                        new_A[i] = new_A[j]
            
            # Check if all values are positive
            valid = True
            for val in new_A:
                if val <= 0:
                    valid = False
                    break
            if valid:
                results.append("YES")
                results.append(' '.join(map(str, new_A)))
            else:
                results.append("NO")
    
    print('\n'.join(results))