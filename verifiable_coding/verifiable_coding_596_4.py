import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        if N == 0:
            results.append(0)
            continue
        
        # For N > 0, find the K-th occurrence
        # The first occurrence is in the first round (k=1)
        # The second occurrence is in the second round (k=2)
        # ...
        # The K-th occurrence is in the K-th round
        # But for even K, it's on the way back, for odd K, it's on the way out
        
        # Time to reach N for the K-th time
        # For K-th round:
        # Time to go from 0 to N: N seconds
        # Time to go back from N to 0: N seconds
        # Total time for one round: 2*N seconds
        # But for K-th round, we need to calculate the time to reach N for the K-th time
        
        # For K-th occurrence:
        # If K is odd, it's on the way out (first time in the K-th round)
        # If K is even, it's on the way back (second time in the K-th round)
        
        # Time for K-1 full rounds: 2 * (N) * (K-1)
        # Then, for the K-th round:
        # If K is odd: time to go from 0 to N: N seconds
        # If K is even: time to go from N to 0: N seconds, but we need to find the time when he reaches N again on the way back
        
        # For K-th round:
        # Time for K-1 full rounds: 2 * (N) * (K-1)
        # Then, for the K-th round:
        # If K is odd: time to reach N is N seconds
        # If K is even: time to reach N is 2*N - (K-1)*N = N*(2 - (K-1)) = N*(1 - K + 2) = N*(3 - K)
        
        # Wait, let's think again:
        # For the K-th round:
        # Time to go from 0 to N: N seconds
        # Time to go back from N to 0: N seconds
        # So, the first time N is reached in the K-th round is at time N seconds
        # The second time N is reached in the K-th round is at time 2*N seconds
        # But for the K-th occurrence, it's either the first or second time in the K-th round
        
        # For K-th occurrence:
        # If K is odd: it's the first time in the K-th round
        # If K is even: it's the second time in the K-th round
        
        # So, the time is:
        # For K-th occurrence:
        # time = (2 * (K-1) * N) + N if K is odd
        # time = (2 * (K-1) * N) + 2 * N if K is even
        
        # Simplify:
        # time = 2 * (K-1) * N + N * (1 if K is odd else 2)
        # time = 2 * (K-1) * N + N * (1 + (K % 2 == 0))
        
        # But for K-th occurrence:
        # If K is odd: it's the first time in the K-th round
        # So, time = 2 * (K-1) * N + N = 2 * N * (K-1) + N = N * (2K - 2 + 1) = N * (2K - 1)
        # If K is even: it's the second time in the K-th round
        # So, time = 2 * (K-1) * N + 2 * N = 2 * N * (K-1 + 1) = 2 * N * K
        
        # So the formula is:
        if K % 2 == 1:
            time = N * (2 * K - 1)
        else:
            time = 2 * N * K
        
        results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()