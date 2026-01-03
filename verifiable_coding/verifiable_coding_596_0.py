import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        if N == 0:
            results.append(0)
            continue
        
        # For N to be visited K-th time
        # First occurrence is in round 1
        # Second occurrence is in round 2
        # ...
        # K-th occurrence is in round K
        # So the K-th time he reaches N is during the K-th round
        
        # Time to reach N for the K-th time
        # The K-th round is the round where he goes from 0 to K and back
        # So the K-th time he reaches N is when he is going from K to K-1
        # So the time is:
        # Time to reach K in the K-th round: 2*K - 1
        # Then he goes back from K to K-1, which takes 1 second per step
        # So to reach N from K, he has to go back K - N steps
        # So total time is (2*K - 1) + (K - N)
        # Which is 3*K - N - 1
        
        time = (3 * K - N - 1) % MOD
        results.append(time)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()