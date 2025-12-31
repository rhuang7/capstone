import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        X = int(input[idx])
        K = int(input[idx+1])
        idx += 2
        
        # Find factors of X
        factors_x = set()
        for i in range(1, int(math.isqrt(X)) + 1):
            if X % i == 0:
                factors_x.add(i)
                factors_x.add(X // i)
        factors_x = sorted(factors_x)
        
        # Compute sum of Kth power of factors of X
        sum_k_power = sum(x**K for x in factors_x)
        
        # Find factors of K
        factors_k = set()
        for i in range(1, int(math.isqrt(K)) + 1):
            if K % i == 0:
                factors_k.add(i)
                factors_k.add(K // i)
        factors_k = sorted(factors_k)
        
        # Compute sum of X times factors of K
        sum_x_times = sum(X * k for k in factors_k)
        
        # Output the results
        print(f"{sum_k_power} {sum_x_times}")

if __name__ == '__main__':
    solve()