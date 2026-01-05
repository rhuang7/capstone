import sys
import math
from collections import defaultdict

def get_distinct_three_digit_numbers(number):
    digits = list(str(number))
    unique_digits = set(digits)
    if len(unique_digits) < 3:
        return 0
    count = 0
    for i in range(100, 1000):
        s = str(i)
        if len(set(s)) == 3 and all(c in unique_digits for c in s):
            count += 1
    return count

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        K = int(input[idx])
        N = int(input[idx+1])
        idx += 2
        
        # Initial number
        current = K
        seen = set()
        seen.add(current)
        total = 0
        
        for _ in range(N):
            # Multiply by 13, 11, 7
            current = current * 13 * 11 * 7
            # Get all distinct 3-digit numbers from the digits
            total += get_distinct_three_digit_numbers(current)
            # Add to seen set
            seen.add(current)
        
        print(len(seen))

if __name__ == '__main__':
    solve()