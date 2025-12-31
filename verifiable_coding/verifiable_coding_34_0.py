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
        # But we need to maximize the number of digits and also the value
        # The best way is to use as many 1s as possible, since they use 2 segments
        # But we can also use 7 (which uses 3 segments) to make the number larger
        # So we try to use as many 7s as possible, then fill with 1s
        # However, the optimal is to use as many 1s as possible, since they are the smallest digit but use the least segments
        # Wait, no. The largest number is the one with the most digits, and the digits should be as large as possible
        # The best approach is to use as many 7s as possible, then fill with 1s
        # Because 7 is the largest digit and uses 3 segments, which is more than 2 (for 1)
        # So we try to use as many 7s as possible, then fill with 1s
        # But wait, 7 uses 3 segments, and 1 uses 2. So for n segments, the maximum number of digits is n // 2
        # But we want to maximize the value, so we should use as many 7s as possible, then fill with 1s
        # Let's try this approach:
        max_digits = n // 2
        # Try to use as many 7s as possible
        # Each 7 uses 3 segments, so we can use floor(n / 3) 7s
        # Then the remaining segments can be used for 1s
        # But this may not be optimal. Let's try to find the best combination
        # The best way is to use as many 7s as possible, then fill with 1s
        # But we can also try to use some 7s and some 1s to maximize the value
        # The optimal is to use as many 7s as possible, then fill with 1s
        # So let's try that
        num_7 = n // 3
        rem = n % 3
        if rem == 0:
            res = '7' * num_7
        else:
            # We can use one 1 and the rest 7s
            res = '7' * (num_7 - 1) + '1' * rem
        print(res)

if __name__ == '__main__':
    solve()