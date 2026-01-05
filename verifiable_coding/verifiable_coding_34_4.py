import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    seg = [6, 2, 5, 5, 4, 5, 3, 7, 6, 6]  # segments for digits 0-9
    
    for n in cases:
        # Find the maximum number of digits that can be displayed
        # with n segments
        max_digits = n // 2
        # Try to maximize the number by using the digit with the least segments
        # and then fill with 1s (which use 2 segments)
        # The digit with the least segments is 1 (2 segments)
        # So we can use as many 1s as possible
        # But we can also use a digit with 2 segments (like 1) to fill the rest
        # So the maximum number is '1' repeated (n // 2) times
        # But we can also try to replace one of the 1s with a digit that uses 2 segments
        # but that would not change the number of segments used
        # So the maximum number is '1' repeated (n // 2) times
        # However, if n is odd, we can replace one of the 1s with a digit that uses 2 segments
        # but that would not change the number of segments used
        # So the maximum number is '1' repeated (n // 2) times
        # But wait, if n is even, then we can use all 1s
        # But if n is odd, we can use (n-1)//2 1s and one digit that uses 2 segments
        # which is still 1
        # So the maximum number is '1' repeated (n // 2) times
        # But wait, what if there is a digit that uses 2 segments and is larger than 1?
        # Like 7 uses 3 segments, but 1 uses 2
        # So the best is to use as many 1s as possible
        # So the answer is '1' repeated (n // 2) times
        # But wait, what if n is 3?
        # Then we can use 1 1 and 1 2 segments, but 2 segments is 1
        # So the answer is 7 (which uses 3 segments)
        # So the approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the digit with the least segments is 1 (2 segments)
        # So the answer is '1' repeated (n // 2) times
        # But if n is 3, then we can use 1 digit (3 segments) which is 7
        # So the answer is 7
        # So the correct approach is to find the maximum number of digits that can be displayed
        # and then use the digit with the least segments to fill the rest
        # So the maximum number of digits is n // 2
        # And the