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
            prefixA[i+1] = (prefixA[i] + A[i]) % MOD
        for i in range(M):
            prefixB[i+1] = (prefixB[i] + B[i]) % MOD
        
        # For each query
        for __ in range(Q):
            query_type = data[idx]
            if query_type == b'1':
                L = int(data[idx+1])
                R = int(data[idx+2])
                X = int(data[idx+3])
                idx += 4
                # Update A's prefix sum
                prefixA[L] = (prefixA[L] - A[L-1] + X) % MOD
                prefixA[R+1] = (prefixA[R+1] - A[R] + X) % MOD
                for i in range(L, R+1):
                    A[i-1] = (A[i-1] + X) % MOD
            elif query_type == b'2':
                L = int(data[idx+1])
                R = int(data[idx+2])
                X = int(data[idx+3])
                idx += 4
                # Update B's prefix sum
                prefixB[L] = (prefixB[L] - B[L-1] + X) % MOD
                prefixB[R+1] = (prefixB[R+1] - B[R] + X) % MOD
                for i in range(L, R+1):
                    B[i-1] = (B[i-1] + X) % MOD
            else:
                # Compute score
                sumA = prefixA[N]
                sumB = prefixB[M]
                res = (sumA * sumB) % MOD
                results.append(str(res))
                idx += 1
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()