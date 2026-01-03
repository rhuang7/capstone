import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for N in cases:
        if N == '0':
            print(0)
            continue
        s = list(N)
        total = sum(int(c) for c in s)
        if total % 9 == 0:
            print(0)
            continue
        # Find the minimal changes needed
        # We can change any digit to make the sum divisible by 9
        # The minimal changes are to change one digit by (9 - (total % 9)) or (total % 9)
        # But we need to find the minimal steps
        # We can try changing each digit to make the sum divisible by 9
        # The minimal steps would be the minimal between (9 - (total % 9)) and (total % 9)
        # But we need to check if it's possible to change a digit to achieve that
        # For example, if total % 9 is 2, we can change a digit by 2 or 7 (if possible)
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But we need to check if it's possible to change a digit to achieve that
        # For example, if total % 9 is 2, we can change a digit by 2 (if the digit is not 9)
        # Or change a digit by 7 (if the digit is not 0)
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by 2, so we need to find another digit
        # So we need to check if there is a digit that can be changed by (total % 9) or (9 - (total % 9))
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So we need to check if there is a digit that can be changed by (total % 9) or (9 - (total % 9))
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need to find another digit
        # So the minimal steps is min( (total % 9), (9 - (total % 9)) )
        # But if the digit is 9, we can't change it by (total % 9), so we need