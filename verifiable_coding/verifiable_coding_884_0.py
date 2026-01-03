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
        factors_X = []
        for i in range(1, int(X**0.5) + 1):
            if X % i == 0:
                factors_X.append(i)
                if i != X // i:
                    factors_X.append(X // i)
        factors_X = list(set(factors_X))
        factors_X.sort()
        
        # Compute sum of Kth power of factors of X
        sum_power = sum(x**K for x in factors_X)
        
        # Find factors of K
        factors_K = []
        for i in range(1, int(K**0.5) + 1):
            if K % i == 0:
                factors_K.append(i)
                if i != K // i:
                    factors_K.append(K // i)
        factors_K = list(set(factors_K))
        factors_K.sort()
        
        # Compute sum of X times factors of K
        sum_X_times = sum(X * k for k in factors_K)
        
        results.append(f"{sum_power} {sum_X_times}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()