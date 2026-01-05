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
        # We try to use as many 1's (2 segments) as possible, then adjust
        # because 1 uses 2 segments, and 7 uses 3 segments
        # So the maximum number of digits is floor(n / 2)
        # But we need to check if we can replace some 1's with 7's to get a larger number
        max_digits = n // 2
        # The maximum number is a string of '7's and '1's
        # We try to use as many 7's as possible
        # Each 7 uses 3 segments, so we can use floor((n - 2 * (max_digits - x)) / 3) 7's
        # We try to maximize the number of 7's
        # The best is to use as many 7's as possible, then fill with 1's
        # So the maximum number is '7' * x + '1' * (max_digits - x)
        # We try to find the best x
        best = '1' * max_digits
        for x in range(min(max_digits, n // 3), 0, -1):
            if 3 * x + 2 * (max_digits - x) <= n:
                best = '7' * x + '1' * (max_digits - x)
                break
        print(best)

if __name__ == '__main__':
    solve()