def check(candidate):
    assert candidate("[]][][") == 2
    assert candidate("[[][]]") == 0
    assert candidate("[[][]]][") == 1


def min_swaps_for_bracket_balancing(s):
    if len(s) % 2 != 0:
        return -1  # Length of string must be even for bracket balancing

    left = 0
    right = 0
    swaps = 0

    for char in s:
        if char == '(':
            left += 1
        elif char == ')':
            right += 1

        # If right brackets exceed left brackets, a swap is needed
        if right > left:
            swaps += 1
            # Swap a '(' with a ')'
            left += 1
            right -= 1

    return swaps

check(min_swaps_for_bracket_balancing)