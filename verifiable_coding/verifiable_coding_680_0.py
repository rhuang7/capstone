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
            query_type = data[idx]
            if query_type == b'1':
                L = int(data[idx+1])
                R = int(data[idx+2])
                X = int(data[idx+3])
                idx += 4
                # Update prefix sums for A
                prefixA[L] -= X * (R - L + 1)
                prefixA[R+1] += X * (R - L + 1)
            elif query_type == b'2':
                L = int(data[idx+1])
                R = int(data[idx+2])
                X = int(data[idx+3])
                idx += 4
                # Update prefix sums for B
                prefixB[L] -= X * (R - L + 1)
                prefixB[R+1] += X * (R - L + 1)
            else:
                # Compute current sumA and sumB from prefix sums
                sumA = prefixA[N]
                sumB = prefixB[M]
                score = (sumA * sumB) % MOD
                results.append(score)
                idx += 1
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()