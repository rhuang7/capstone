import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        # The minimum sum of K distinct positive integers is 1 + 2 + ... + K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        if min_sum > N:
            print(-1)
            continue
        
        # The maximum possible gcd is the largest d such that d * K <= N and d * (K*(K+1)//2) <= N
        # So we need to find the maximum d such that d * (K*(K+1)//2) <= N
        # This is equivalent to finding the largest d where d <= N // (K*(K+1)//2)
        max_d = N // (K * (K + 1) // 2)
        
        # Now check if there exists a multiple of max_d that can be used to form K distinct numbers
        # The sum of K distinct numbers with gcd d is d*(1+2+...+K) = d*K*(K+1)//2
        # So we need to check if N is divisible by d
        # But since we are looking for the maximum d, we can start from max_d and go downwards
        # until we find a d that divides N
        
        found = False
        for d in range(max_d, 0, -1):
            if N % d == 0:
                found = True
                break
        
        if found:
            print(d)
        else:
            print(-1)

if __name__ == '__main__':
    solve()