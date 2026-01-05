import sys

def get_distinct_three_digit_numbers(number):
    # Multiply by 13, 11, 7
    result = number * 13 * 11 * 7
    # Convert to string to process digits
    s = str(result)
    # Get all unique digits
    unique_digits = set(s)
    # If there are less than 3 unique digits, return 0
    if len(unique_digits) < 3:
        return 0
    # Generate all permutations of 3 digits
    from itertools import permutations
    perms = set(permutations(unique_digits, 3))
    # Convert back to numbers and check if they are 3-digit
    numbers = set()
    for p in perms:
        num = int(''.join(p))
        if 100 <= num <= 999:
            numbers.add(num)
    return len(numbers)

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        K = int(input[idx])
        N = int(input[idx+1])
        idx += 2
        # First step: process K
        step1 = get_distinct_three_digit_numbers(K)
        # If step1 is 0, no numbers can be generated
        if step1 == 0:
            results.append(0)
            continue
        # For N steps, the numbers will eventually reach a fixed set
        # We simulate up to N steps, but since N can be large, we find the fixed set
        seen = set()
        current_set = set()
        for i in range(N):
            current_set = get_distinct_three_digit_numbers(i)
            if current_set.issubset(seen):
                break
            seen.update(current_set)
        results.append(len(seen))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()