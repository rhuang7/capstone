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
        # Each round k, the position N is visited twice (once going up, once going down)
        # Except for the first round where it's visited once (only at the end)
        # So for K-th time, if K is odd, it's the up direction
        # If K is even, it's the down direction
        
        # For K-th time:
        # If K is odd, it's the up direction (first occurrence in round k)
        # If K is even, it's the down direction (second occurrence in round k)
        
        # Find the round in which the K-th occurrence happens
        if K % 2 == 1:
            # First occurrence in round (K + 1) // 2
            round_num = (K + 1) // 2
        else:
            # Second occurrence in round K // 2
            round_num = K // 2
        
        # Time to reach N for the first time in round round_num
        # Time to go from 0 to N: N seconds
        # Time to go back from N to 0: N seconds
        # But for the first occurrence in round round_num, it's only going up
        # So time is N seconds
        
        # Time to reach N for the K-th time
        # If K is odd: it's the first occurrence in round round_num
        # If K is even: it's the second occurrence in round round_num
        # So total time is:
        # Time to complete all previous rounds (each round takes 2*N seconds)
        # Plus time to reach N in the current round
        
        # Time to complete previous rounds: 2 * (round_num - 1) * round_num
        # Time to reach N in current round: N seconds (for first occurrence)
        # Or 2*N seconds (for second occurrence)
        
        if K % 2 == 1:
            time = 2 * (round_num - 1) * round_num + N
        else:
            time = 2 * (round_num - 1) * round_num + 2 * N
        
        results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()