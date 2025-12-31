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
        # Each round k, the maximum distance is k
        # The number of times N is visited in round k is 2 if k > N, 1 if k == N, 0 if k < N
        # So, the K-th occurrence of N is in round (N + (K-1) // 2)
        # But we need to find the correct round and position in that round
        
        # Find the round where the K-th occurrence of N happens
        # Each round k >= N contributes 2 times to N (except when k = N)
        # So, the number of rounds needed is ceil((K) / 2)
        # But we need to find the exact round where the K-th occurrence is
        # Let's think differently: for N, the first occurrence is in round N
        # Then, for each round after that, it's visited twice
        # So, the K-th occurrence is in round (N + (K-1) // 2)
        # But if K is odd, it's the first occurrence in that round
        # If K is even, it's the second occurrence in that round
        
        # So, the round is:
        round_num = N + (K - 1) // 2
        
        # Now calculate the time to reach N for the K-th time
        # Time to go from 0 to round_num: round_num * 2 - 1
        # Then, for the K-th time, if K is odd, it's the first time in that round (going to N)
        # If K is even, it's the second time in that round (coming back from N)
        
        # Time to reach N for the first time in round_num
        time_to_N = round_num * 2 - 1
        
        # If K is even, it's the second time in that round (coming back from N)
        if K % 2 == 0:
            time_to_N = round_num * 2 - 1 + (round_num - N)
        
        results.append(time_to_N % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()