import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        X = list(map(int, data[idx:idx+N]))
        idx += N
        # Find the latest day Y such that Y is a multiple of X[0], and there exists a day >= Y for each subsequent X[i]
        # The latest possible day is the maximum Y such that Y is a multiple of X[0], and Y + LCM(X[1], ..., X[N-1]) <= D
        # We can use binary search to find Y
        # The LCM of X[1], ..., X[N-1] is the minimum day after Y that Diana can take the next buses
        from math import gcd
        def lcm(a, b):
            return a * b // gcd(a, b)
        l = 1
        for x in X[1:]:
            l = lcm(l, x)
        # Binary search for the latest Y
        low = 1
        high = D
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid % X[0] == 0 and mid + l <= D:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans)

if __name__ == '__main__':
    solve()