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
        
        # For N to be visited K-th time
        # First occurrence is in round 1
        # Then every even round (2, 4, 6, ...) contributes an additional occurrence
        # So, if K is odd, it's in the (K+1)//2-th round
        # If K is even, it's in the K//2-th round
        if K % 2 == 1:
            round_num = (K + 1) // 2
        else:
            round_num = K // 2
        
        # Time to reach N for the first time in round_num
        # Time to go from 0 to N: N seconds
        # Time to go back from N to 0: N seconds
        # But we only need to go to N once in the round
        # So total time is (round_num - 1) * (2 * N) + N
        time = (round_num - 1) * (2 * N) + N
        
        results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()