import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for N in cases:
        s = N.decode()
        total = sum(int(c) for c in s)
        if total % 9 == 0:
            print(0)
            continue
        # Find the minimal steps to make the sum of digits a multiple of 9
        # The minimal steps is the minimal difference between the current sum and the nearest multiple of 9
        remainder = total % 9
        if remainder == 0:
            print(0)
        else:
            # We can either subtract remainder or add (9 - remainder)
            # But since we can only change one digit, we need to find the minimal steps
            # The minimal steps is the minimal between remainder and 9 - remainder
            # However, we can't change a digit to 0 if it's the first digit
            # So we need to check if there is a digit that can be changed to decrease the sum by remainder or increase by (9 - remainder)
            # But since we can only change one digit, we can find the minimal steps by checking the minimal steps to change one digit
            # The minimal steps is the minimal between remainder and 9 - remainder
            # But we need to make sure that there is at least one digit that can be changed
            # So the answer is min(remainder, 9 - remainder)
            print(min(remainder, 9 - remainder))

if __name__ == '__main__':
    solve()