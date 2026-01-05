import sys

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        if N == 0:
            print(0)
            continue
        
        # For N, the first time is when he goes from 0 to N in the Nth round
        # The second time is when he comes back from N to 0 in the Nth round
        # The third time is when he goes from 0 to N in the (N+1)th round
        # And so on
        
        # Find the round in which the Kth occurrence of N happens
        # The first occurrence is in round N
        # The second occurrence is in round N
        # The third occurrence is in round N+1
        # The fourth occurrence is in round N+1
        # So for Kth occurrence, if K is odd, it's in round (N + (K-1)//2)
        # If K is even, it's in round (N + (K//2))
        
        # For Kth occurrence, the round is:
        round_num = N + (K + 1) // 2 - 1
        
        # Time to reach N for the Kth time
        # Time to go from 0 to N in round_num: (N * 2 - 1) steps
        # Time to go from N to 0 in round_num: (N * 2 - 1) steps
        # Time to go from 0 to N in round_num + 1: (N * 2 - 1) steps
        # So for Kth occurrence:
        # If K is odd: it's the (K+1)//2 th time going from 0 to N
        # If K is even: it's the K//2 th time coming back from N to 0
        
        if K % 2 == 1:
            # Odd K: going from 0 to N
            time = (N * 2 - 1) * ((K + 1) // 2)
        else:
            # Even K: coming back from N to 0
            time = (N * 2 - 1) * (K // 2) + (N * 2 - 1)
        
        print(time % MOD)

if __name__ == '__main__':
    solve()