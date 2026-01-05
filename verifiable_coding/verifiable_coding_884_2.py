import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        X = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # Find factors of X
        factors_x = []
        for i in range(1, int(X**0.5) + 1):
            if X % i == 0:
                factors_x.append(i)
                if i != X // i:
                    factors_x.append(X // i)
        factors_x = list(set(factors_x))
        factors_x.sort()
        
        # Sum of Kth power of factors of X
        sum_k_power = sum(x**K for x in factors_x)
        
        # Find factors of K
        factors_k = []
        for i in range(1, int(K**0.5) + 1):
            if K % i == 0:
                factors_k.append(i)
                if i != K // i:
                    factors_k.append(K // i)
        factors_k = list(set(factors_k))
        factors_k.sort()
        
        # Sum of X times of factors of K
        sum_x_times = sum(X * k for k in factors_k)
        
        results.append(f"{sum_k_power} {sum_x_times}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()