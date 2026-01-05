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
    # We'll use a dictionary to store for each R, the list of cities visited and the product
    # But for large N and Q, this is not efficient. So we need a better way.
    # Instead, for each query of type 2, we'll compute the product on the fly.
    
    # For fast I/O
    output = []
    
    for _ in range(Q):
        t = int(data[idx])
        idx += 1
        if t == 1:
            p = int(data[idx])
            f = int(data[idx+1])
            idx += 2
            F[p-1] = f
        else:
            R = int(data[idx])
            idx += 1
            # Compute the path
            cities = []
            current = 1
            while current <= N:
                cities.append(current)
                current += R
            # Compute product
            product = 1
            for city in cities:
                product = (product * F[city-1]) % MOD
            # Compute first digit
            first = first_digit(product)
            output.append(f"{first} {product}")
    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()