import sys
import math
from itertools import permutations

def get_distinct_three_digit_numbers(number):
    digits = list(str(number))
    unique_digits = set(digits)
    if len(unique_digits) < 3:
        return 0
    count = 0
    for p in permutations(unique_digits, 3):
        num = int(''.join(p))
        if 100 <= num <= 999:
            count += 1
    return count

def process_number(number):
    result = number * 13 * 11 * 7
    return result

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        K = int(data[index])
        N = int(data[index+1])
        index += 2
        
        # Initial step
        current = K
        seen = set()
        total = 0
        for step in range(N + 1):
            current = process_number(current)
            distinct = get_distinct_three_digit_numbers(current)
            if distinct > 0:
                total += distinct
            seen.add(current)
        
        print(total)

if __name__ == '__main__':
    solve()