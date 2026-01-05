import sys

def get_distinct_three_digit_numbers(number):
    # Multiply by 13, 11, 7
    result = number * 13 * 11 * 7
    # Convert to string to process digits
    result_str = str(result)
    # Get all unique digits
    unique_digits = set(result_str)
    # If there are less than 3 unique digits, return 0
    if len(unique_digits) < 3:
        return 0
    # Generate all possible 3-digit numbers from the unique digits
    from itertools import permutations
    distinct_numbers = set()
    for p in permutations(unique_digits):
        if p[0] != '0':
            distinct_numbers.add(int(''.join(p)))
    return len(distinct_numbers)

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        K = int(input[idx])
        N = int(input[idx+1])
        idx += 2
        # Initial step
        current = K
        seen = set()
        count = 0
        for step in range(N + 1):
            # Get all distinct 3-digit numbers from current
            numbers = get_distinct_three_digit_numbers(current)
            # Add to seen
            for num in range(100, 1000):
                if str(num) in seen:
                    continue
                seen.add(str(num))
            # If no new numbers, break
            if numbers == 0:
                break
            # Update current to the first number in the set
            current = next(iter(seen))
        print(len(seen))

if __name__ == '__main__':
    solve()