import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for N in cases:
        if int(N) % 9 == 0:
            print(0)
            continue
        # Calculate the sum of digits
        s = sum(int(c) for c in N)
        # The required sum to make it divisible by 9 is s % 9
        # We need to change one digit to make the total sum divisible by 9
        # The minimum number of seconds is the minimum of (s % 9) or (9 - (s % 9))
        # But since we can only change one digit, we need to find the minimum steps to adjust one digit
        # The minimum steps is the minimum between (s % 9) and (9 - (s % 9))
        # But if the sum is already divisible by 9, we do nothing
        rem = s % 9
        if rem == 0:
            print(0)
        else:
            print(min(rem, 9 - rem))
            
if __name__ == '__main__':
    solve()