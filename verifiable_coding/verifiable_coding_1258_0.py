import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for N in cases:
        if int(N) % 9 == 0:
            print(0)
            continue
        # Calculate the sum of digits
        s = sum(int(c) for c in N)
        # The required sum to make it divisible by 9 is s % 9
        # We can either subtract or add to make it divisible by 9
        # The minimum steps is the minimum between (s % 9) and (9 - (s % 9))
        # But since we can only change one digit at a time, we need to find the minimum steps to change one digit to make the sum divisible by 9
        # So the minimum steps is the minimum between (s % 9) and (9 - (s % 9))
        # But since we can only change one digit, the minimum steps is the minimum between (s % 9) and (9 - (s % 9))
        # However, if the sum is already divisible by 9, we do nothing
        remainder = s % 9
        if remainder == 0:
            print(0)
        else:
            print(min(remainder, 9 - remainder))
            
if __name__ == '__main__':
    solve()