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
        # Add the reversed numbers as integers
        sum_rev = int(a_rev) + int(b_rev)
        # Reverse the sum and remove leading zeros
        result = str(sum_rev)[::-1].lstrip('0')
        print(result)

if __name__ == '__main__':
    solve()