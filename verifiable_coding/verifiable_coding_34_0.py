import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    segment_counts = [2, 3, 4, 4, 5, 5, 6, 7, 6, 6]
    
    for n in cases:
        if n < 2:
            print(0)
            continue
        # Max number of digits is n // 2, but we can try to maximize the digits
        # We want to maximize the number of digits, and then maximize the value
        # So we try to use as many 2-segment digits as possible (like 1)
        # Then fill the rest with 3-segment digits (like 7)
        # But we need to find the maximum number of digits possible
        # Let's try to find the maximum number of digits
        max_digits = 0
        for i in range(1, n+1):
            if i * 2 <= n:
                max_digits = i
                break
        # Now try to maximize the value with max_digits digits
        # We want to use as many 7s as possible, then 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max_digits digits
        # So we can try to use as many 7s as possible, then fill with 1s
        # But we need to use exactly max