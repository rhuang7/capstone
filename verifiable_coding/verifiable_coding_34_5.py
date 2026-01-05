import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    seg = [6, 2, 5, 5, 4, 5, 3, 7, 6, 6]  # segments for digits 0-9
    
    for n in cases:
        # Find the maximum number of digits we can display
        # Each digit uses at least 2 segments (digit 1)
        max_digits = n // 2
        # Try to replace some digits with ones that use fewer segments
        # Start with all digits as 1 (uses 2 segments each)
        res = '1' * max_digits
        # Try to replace some digits with 0 (uses 6 segments)
        # Each replacement saves 4 segments (2 -> 6)
        # So we can replace up to (n - 2 * max_digits) // 4 digits
        # But we can't replace more than max_digits
        replace = min(max_digits, (n - 2 * max_digits) // 4)
        res = '0' * replace + '1' * (max_digits - replace)
        print(res)

if __name__ == '__main__':
    solve()