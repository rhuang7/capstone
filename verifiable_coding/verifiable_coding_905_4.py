import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().strip()
    n = int(input)
    
    if n == 1:
        print(1)
        return
    
    # Josephus problem solution
    # The safe position for n people is 2 * (n - 2^floor(log2(n))) + 1
    # Find the largest power of 2 less than or equal to n
    l = 1
    while l * 2 <= n:
        l *= 2
    
    result = 2 * (n - l) + 1
    print(result)

if __name__ == '__main__':
    solve()