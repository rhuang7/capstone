import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().strip()
    n = int(input)
    
    if n == 1:
        print(1)
        return
    
    # Josephus problem solution
    # The safe position for n people is 2 * (n - 2^floor(log2(n))) + 1
    # Find the largest power of 2 less than or equal to n
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid << 1 > n:
            high = mid
        else:
            low = mid + 1
    power_of_two = low
    safe_position = 2 * (n - power_of_two) + 1
    print(safe_position)

if __name__ == '__main__':
    solve()