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
        # Each round k, the position N is visited twice (once going up, once going down)
        # Except for the first time when k = N, it's only visited once
        # So for K-th time, if K is odd, it's the first time in some round
        # If K is even, it's the second time in some round
        
        # Find the round where N is visited K-th time
        if K % 2 == 1:
            # First occurrence in some round
            round_num = (K + 1) // 2
        else:
            # Second occurrence in some round
            round_num = K // 2
        
        # Time to reach N for the K-th time
        # Time to go up to N in round_num
        time_up = 2 * (round_num - 1) + 2 * N - 1
        # Time to go down to N in round_num
        time_down = 2 * (round_num - 1) + 2 * N - 1 + 2 * N - 1
        
        if K % 2 == 1:
            results.append(time_up % MOD)
        else:
            results.append(time_down % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()