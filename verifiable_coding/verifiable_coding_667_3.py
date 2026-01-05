import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        X = list(map(int, data[idx:idx+N]))
        idx += N
        # Find the latest day Y such that Y is a multiple of X[0], and there exists a day >= Y for each subsequent X[i]
        # The latest possible day is the maximum Y such that Y is a multiple of X[0], and Y + LCM(X[1], ..., X[N-1]) <= D
        # We can use binary search on Y
        from math import gcd
        from functools import reduce
        def lcm(a, b):
            return a * b // gcd(a, b)
        lcm_rest = reduce(lcm, X[1:])
        # The latest possible Y is D - (D % X[0]) if D % X[0] != 0 else D
        # But we need to ensure that Y + lcm_rest <= D
        # So the maximum Y is D - (lcm_rest % X[0]) if D % X[0] != 0 else D
        # But we need to find the maximum Y such that Y is a multiple of X[0] and Y + lcm_rest <= D
        # So Y can be at most D - lcm_rest
        # But Y must be a multiple of X[0]
        # So the maximum Y is the largest multiple of X[0] <= D - lcm_rest
        # If D - lcm_rest < X[0], then it's impossible, but the problem says it's guaranteed
        max_y = D - lcm_rest
        if max_y < X[0]:
            max_y = X[0]
        # Find the largest multiple of X[0] <= max_y
        # It is max_y - (max_y % X[0]) if max_y % X[0] != 0 else max_y
        if max_y % X[0] != 0:
            max_y -= max_y % X[0]
        results.append(str(max_y))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()