import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    A.sort()
    
    left = A[0]
    right = A[-1]
    
    # Since K is small (1, 2, 3), we can use ternary search
    def f(x):
        res = 0
        for a in A:
            diff = x - a
            res += abs(diff ** K)
        return res
    
    def ternary_search(l, r):
        while r - l > 3:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            f1 = f(m1)
            f2 = f(m2)
            if f1 < f2:
                r = m2 - 1
            else:
                l = m1 + 1
        # Check all values in [l, r]
        min_val = float('inf')
        for i in range(l, r + 1):
            if f(i) < min_val:
                min_val = f(i)
        # Find the smallest x with min_val
        for i in range(l, r + 1):
            if f(i) == min_val:
                return i
        return l
    
    result = ternary_search(left, right)
    print(result)

if __name__ == '__main__':
    solve()