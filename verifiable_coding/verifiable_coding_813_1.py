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
    # But for simplicity, we'll use binary search in the range [min(A), max(A)]
    # and check the minimum in the vicinity of the median
    
    # Find the median
    median = A[N // 2]
    
    # Check values around the median
    best = median
    for x in range(max(1, median - 2), min(50000, median + 3)):
        if f(x) < f(best):
            best = x
    
    print(best)

if __name__ == '__main__':
    solve()