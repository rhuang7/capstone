import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().strip()
    n = int(input)
    
    if n == 1:
        print(1)
        return
    
    # Josephus problem solution
    # The safe position is 2*(n - 2^floor(log2(n))) + 1
    # Find the largest power of 2 less than or equal to n
    low = 1
    high = 1
    while high < n:
        high <<= 1
    
    print(2 * (n - high) + 1)

if __name__ == '__main__':
    solve()