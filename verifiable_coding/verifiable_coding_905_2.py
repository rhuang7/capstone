import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().strip()
    n = int(input)
    
    if n == 1:
        print(1)
        return
    
    # Josephus problem solution for every second person eliminated
    # The safe position is 2*(n - 2^m) + 1, where 2^m is the largest power of 2 less than or equal to n
    m = 0
    while (1 << (m + 1)) <= n:
        m += 1
    power_of_two = 1 << m
    safe_position = 2 * (n - power_of_two) + 1
    print(safe_position)

if __name__ == '__main__':
    solve()