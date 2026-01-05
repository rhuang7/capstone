import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, M, K = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        restrictions = []
        for _ in range(M):
            typ = data[idx]
            L = int(data[idx+1])
            R = int(data[idx+2])
            restrictions.append((typ, L, R))
            idx += 3
        
        # Initialize the array with -1
        A = [ -1 for _ in range(N) ]
        
        # Process the original array
        for i in range(N):
            if A[i] != -1:
                if A[i] < 1 or A[i] > K:
                    results.append(0)
                    break
        else:
            # Process restrictions
            # We'll use a difference array to track the constraints
            diff = [0] * (N + 2)
            
            for typ, L, R in restrictions:
                if typ == 'I':
                    # Ai - Ai-1 = 1 => Ai = Ai-1 + 1
                    # So diff[L] += 1, diff[R+1] -= 1
                    diff[L] += 1
                    diff[R + 1] -= 1
                else:
                    # Ai - Ai-1 = -1 => Ai = Ai-1 - 1
                    # So diff[L] -= 1, diff[R + 1] += 1
                    diff[L] -= 1
                    diff[R + 1] += 1
            
            # Compute the cumulative differences
            current = 0
            for i in range(1, N + 1):
                current += diff[i]
                if current < 0:
                    results.append(0)
                    break
                # Check if the current difference is valid
                if i > 1:
                    if A[i - 1] != -1 and A[i - 1] + current > K:
                        results.append(0)
                        break
                    if A[i - 1] == -1 and current < 1:
                        results.append(0)
                        break
                # Update the current value
                if A[i - 1] == -1:
                    A[i - 1] = current
                else:
                    if A[i - 1] + current != A[i - 1]:
                        results.append(0)
                        break
            else:
                # Check if all elements are within bounds
                valid = True
                for val in A:
                    if val != -1 and (val < 1 or val > K):
                        valid = False
                        break
                if valid:
                    # Compute the number of ways
                    # The number of ways is the product of the number of choices for each unknown element
                    # Each unknown element can be chosen in (K - (current value)) ways
                    # But we need to compute the product of (K - (current value)) for each unknown element
                    # However, we need to track the current value for each position
                    # We'll compute the current value for each position
                    current = 0
                    ways = 1
                    for i in range(N):
                        if A[i] == -1:
                            # The current value is the accumulated difference up to this position
                            # We need to compute it
                            current = 0
                            for j in range(1, i + 1):
                                current += diff[j]
                            # The value at position i is current
                            # The number of choices is K - current + 1
                            ways = (ways * (K - current + 1)) % MOD
                        else:
                            # Check if the value is valid
                            if A[i] < 1 or A[i] > K:
                                valid = False
                                break
                    if valid:
                        results.append(ways)
                    else:
                        results.append(0)
                else:
                    results.append(0)
        continue
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()