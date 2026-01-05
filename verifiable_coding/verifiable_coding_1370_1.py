import sys
import math
from itertools import permutations

def get_distinct_three_digit_numbers(number):
    digits = list(str(number))
    unique_digits = set(digits)
    if len(unique_digits) < 3:
        return 0
    result = set()
    for p in permutations(unique_digits):
        num = int(''.join(p))
        if 100 <= num <= 999:
            result.add(num)
    return len(result)

def process_number(number):
    multiplied = number * 13 * 11 * 7
    return get_distinct_three_digit_numbers(multiplied)

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
        current = K
        seen = set()
        count = 0
        for step in range(N):
            current = process_number(current)
            if current in seen:
                break
            seen.add(current)
            count += 1
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()