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
    
    # Ternary search
    def find_min():
        low = left
        high = right
        while high - low > 3:
            m1 = low + (high - low) // 3
            m2 = high - (high - low) // 3
            f1 = f(m1)
            f2 = f(m2)
            if f1 < f2:
                high = m2
            else:
                low = m1
        # Check all values in [low, high]
        min_val = float('inf')
        for x in range(low, high + 1):
            if f(x) < min_val:
                min_val = f(x)
        # Find the smallest x with min_val
        for x in range(low, high + 1):
            if f(x) == min_val:
                return x
        return low
    
    print(find_min())

if __name__ == '__main__':
    solve()