import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # The minimum sum of K distinct positive integers is 1 + 2 + ... + K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        
        if min_sum > N:
            print(-1)
            continue
        
        # The maximum possible gcd is the largest divisor of N that is <= (N - min_sum) // K
        # We need to find the maximum d such that d * K <= N and d * (K*(K+1)//2) <= N
        # So d <= (N - min_sum) // K
        max_d = (N - min_sum) // K
        
        # Find the maximum divisor of N that is <= max_d
        # We iterate from max_d down to 1 and check if it divides N
        # If we find such a d, then it's the answer
        # Otherwise, -1
        for d in range(min(max_d, N), 0, -1):
            if N % d == 0:
                print(d)
                break
        else:
            print(-1)

if __name__ == '__main__':
    solve()