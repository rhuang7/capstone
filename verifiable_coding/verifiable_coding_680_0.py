import sys
import math

MOD = 998244353

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+M]))
        idx += M
        Q = int(data[idx])
        idx += 1
        
        # Precompute prefix sums for A and B
        prefixA = [0] * (N + 1)
        prefixB = [0] * (M + 1)
        for i in range(N):
            prefixA[i+1] = prefixA[i] + A[i]
        for i in range(M):
            prefixB[i+1] = prefixB[i] + B[i]
        
        # Compute initial score
        sumA = sum(A)
        sumB = sum(B)
        score = (sumA * sumB) % MOD
        results.append(score)
        
        for __ in range(Q):
            query_type = int(data[idx])
            idx += 1
            if query_type == 1:
                L = int(data[idx]) - 1
                R = int(data[idx+1]) - 1
                X = int(data[idx+2])
                idx += 3
                # Update prefixA
                prefixA[L+1] += X * (R - L + 1)
                for i in range(L+1, R+2):
                    prefixA[i] += X
                # Update sumA
                sumA += X * (R - L + 1)
            elif query_type == 2:
                L = int(data[idx]) - 1
                R = int(data[idx+1]) - 1
                X = int(data[idx+2])
                idx += 3
                # Update prefixB
                prefixB[L+1] += X * (R - L + 1)
                for i in range(L+1, R+2):
                    prefixB[i] += X
                # Update sumB
                sumB += X * (R - L + 1)
            else:
                # Query type 3
                res = (sumA * sumB) % MOD
                results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()