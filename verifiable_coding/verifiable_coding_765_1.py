import sys
import math

MOD = 10**9 + 7

def first_digit(x):
    while x >= 10:
        x //= 10
    return x

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    
    F = list(map(int, data[idx:idx+N]))
    idx += N
    
    Q = int(data[idx])
    idx += 1
    
    # Preprocess for each R, the path and product
    # Since R can be up to N, and N is 1e5, we can't precompute for all R
    # So we process each query on the fly
    
    for _ in range(Q):
        type_q = int(data[idx])
        idx += 1
        if type_q == 1:
            p = int(data[idx]) - 1  # 0-based
            idx += 1
            f = int(data[idx])
            idx += 1
            F[p] = f
        else:
            R = int(data[idx])
            idx += 1
            # Compute the path
            path = []
            current = 1
            while current <= N:
                path.append(current - 1)  # 0-based
                current += R
            # Compute product
            product = 1
            for i in path:
                product = (product * F[i]) % MOD
            # Compute first digit
            first = first_digit(product)
            print(first, product % MOD)
            
if __name__ == '__main__':
    solve()