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
        for i in range(N):
            prefixA[i+1] = (prefixA[i] + A[i]) % MOD
        
        prefixB = [0] * (M + 1)
        for i in range(M):
            prefixB[i+1] = (prefixB[i] + B[i]) % MOD
        
        # Initialize the sum of A and B
        sumA = sum(A) % MOD
        sumB = sum(B) % MOD
        
        # Compute the initial score
        score = (sumA * sumB) % MOD
        
        for __ in range(Q):
            query_type = int(data[idx])
            idx += 1
            
            if query_type == 1:
                L = int(data[idx]) - 1
                R = int(data[idx+1]) - 1
                X = int(data[idx+2])
                idx += 3
                
                # Update the sumA
                sumA = (sumA + X * (R - L + 1)) % MOD
                
            elif query_type == 2:
                L = int(data[idx]) - 1
                R = int(data[idx+1]) - 1
                X = int(data[idx+2])
                idx += 3
                
                # Update the sumB
                sumB = (sumB + X * (R - L + 1)) % MOD
                
            else:
                # Print the score
                print(score % MOD)
                
                # Update the score based on current sumA and sumB
                score = (sumA * sumB) % MOD

if __name__ == '__main__':
    main()