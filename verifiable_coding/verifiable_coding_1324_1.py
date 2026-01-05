import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        # The minimum sum of K distinct positive integers is 1+2+...+K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        if min_sum > N:
            results.append(-1)
            continue
        
        # The maximum possible gcd is the maximum d such that d * (1+2+...+K) <= N
        # So d_max = N // min_sum
        d_max = N // min_sum
        # Now check if there exists a d <= d_max such that d * (1+2+...+K) <= N and d is a divisor of N
        # The maximum such d is the answer
        # We need to find the maximum d <= d_max that divides N
        # So we check from d_max down to 1
        found = -1
        for d in range(d_max, 0, -1):
            if N % (d * min_sum) == 0:
                found = d
                break
        results.append(found)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()