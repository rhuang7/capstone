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
        # The first time is when he goes to N in the N-th round
        # The second time is when he comes back from N in the N-th round
        # The third time is when he goes to N in the (N+1)-th round
        # The fourth time is when he comes back from N in the (N+1)-th round
        # And so on
        
        # For K-th time:
        # If K is odd: it's the (K+1)//2-th time he goes to N
        # If K is even: it's the K//2-th time he comes back from N
        
        if K % 2 == 1:
            # Going to N
            time = (N - 1) * 2 + 1 + (K + 1) // 2 - 1
        else:
            # Coming back from N
            time = (N - 1) * 2 + 1 + (K // 2) - 1
        
        results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()