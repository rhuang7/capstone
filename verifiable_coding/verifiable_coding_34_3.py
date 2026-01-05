import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    seg = [6, 2, 5, 5, 4, 5, 3, 7, 6, 6]  # segments for digits 0-9
    
    for n in cases:
        # Max number of digits is n // min_segment, where min_segment is 2 (for 1)
        # But we need to maximize the number of digits and then the value
        # So we try to use as many 1s as possible (2 segments each)
        # But we also need to check if we can replace some 1s with higher digits
        # The optimal is to use as many 1s as possible, then replace some with 7 (7 segments)
        # But we need to find the maximum number of digits possible
        # Let's try to find the maximum number of digits possible
        # The maximum number of digits is floor(n / 2)
        # But we can also try to replace some 1s with 7s
        # Let's try to find the maximum number of digits possible
        max_digits = n // 2
        # Now try to replace some 1s with 7s
        # Each 7 uses 7 segments, so we can replace a 1 (2 segments) with a 7 (7 segments)
        # So each replacement uses 5 more segments
        # So the number of replacements is floor((n - 2 * max_digits) / 5)
        # But we can't replace more than max_digits times
        # So the maximum number of 7s is min(max_digits, (n - 2 * max_digits) // 5)
        # The rest are 1s
        # So the maximum number of 7s is min(max_digits, (n - 2 * max_digits) // 5)
        # So the answer is '7' * num_7s + '1' * (max_digits - num_7s)
        # But we need to make sure that the total segments is <= n
        # Let's compute it
        max_digits = n // 2
        rem = n - 2 * max_digits
        num_7s = min(max_digits, rem // 5)
        result = '7' * num_7s + '1' * (max_digits - num_7s)
        print(result)

if __name__ == '__main__':
    solve()