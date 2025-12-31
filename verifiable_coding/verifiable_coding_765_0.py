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

    # Preprocess for each R, the product of the cities visited
    # But since R can be up to N and N is 1e5, we can't precompute for all R
    # So we process each query on the fly

    for _ in range(Q):
        type_query = int(data[idx])
        idx += 1
        if type_query == 1:
            p = int(data[idx])
            idx += 1
            f = int(data[idx])
            idx += 1
            F[p-1] = f
        else:
            R = int(data[idx])
            idx += 1
            # Compute the path: 1, 1+R, 1+2R, ..., 1+iR <= N
            # The cities are 1, 1+R, 1+2R, ..., 1+kR where k is max such that 1+kR <= N
            # So the cities are at positions 1, 1+R, 1+2R, ..., 1+kR
            # The product is product of F[0], F[R], F[2R], ..., F[kR]
            # We need to compute this product modulo MOD and find the first digit
            product = 1
            for i in range(0, N, R):
                product = (product * F[i]) % MOD
            first = first_digit(product)
            print(f"{first} {product}")

if __name__ == '__main__':
    solve()