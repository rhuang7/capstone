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
    
    # Binary search for the optimal x
    def f(x):
        res = 0
        for a in A:
            diff = x - a
            res += abs(diff ** K)
        return res
    
    # Since the function is convex, we can use ternary search
    # We'll search in the range [A[0], A[-1]]
    # But since x can be any integer, we'll search in the range [A[0]-1, A[-1]+1]
    # To ensure we find the minimum, we'll check all integers in this range
    # But for efficiency, we'll use ternary search
    
    # Ternary search
    l = A[0] - 1
    r = A[-1] + 1
    
    while l < r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        f1 = f(m1)
        f2 = f(m2)
        if f1 < f2:
            r = m2 - 1
        else:
            l = m1 + 1
    
    # Check all integers in the range [l, r] to find the minimum
    min_x = l
    min_val = f(l)
    for x in range(l, r + 1):
        val = f(x)
        if val < min_val:
            min_val = val
            min_x = x
        elif val == min_val:
            if x < min_x:
                min_x = x
    
    print(min_x)
    
if __name__ == '__main__':
    solve()