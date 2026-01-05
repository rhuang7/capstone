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
    
    # Ternary search in the range [left, right]
    def find_min():
        l = left
        r = right
        while l < r:
            m1 = l + (r - l) // 3
            m2 = r - (r - l) // 3
            f1 = f(m1)
            f2 = f(m2)
            if f1 < f2:
                r = m2 - 1
            else:
                l = m1 + 1
        return l
    
    x = find_min()
    print(x)

if __name__ == '__main__':
    solve()