import sys
import math
from itertools import permutations

def get_distinct_3_digit_numbers(number):
    digits = list(str(number))
    unique_digits = set(digits)
    if len(unique_digits) < 3:
        return 0
    count = 0
    for p in permutations(unique_digits):
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
    results = []
    for _ in range(T):
        K = int(data[index])
        N = int(data[index+1])
        index += 2
        initial = K
        seen = set()
        seen.add(initial)
        count = 0
        for _ in range(N):
            current = initial
            next_val = process_number(current)
            unique_numbers = get_distinct_3_digit_numbers(next_val)
            count += unique_numbers
            initial = next_val
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()