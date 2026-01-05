import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    idx = 1
    for _ in range(n):
        a = int(input[idx])
        b = int(input[idx+1])
        idx += 2
        # Reverse the numbers
        a_rev = str(a)[::-1]
        b_rev = str(b)[::-1]
        # Convert to integers
        a_int = int(a_rev)
        b_int = int(b_rev)
        # Add them
        sum_int = a_int + b_int
        # Reverse the sum
        sum_rev = str(sum_int)[::-1]
        # Remove leading zeros
        print(sum_rev.lstrip('0') or '0')

if __name__ == '__main__':
    solve()