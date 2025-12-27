def check(candidate):
    assert candidate('112112',6) == 6
    assert candidate('111',3) == 6
    assert candidate('1101112',7) == 12


def count_substrings_with_sum_equal_to_length(s):
    from collections import defaultdict

    count = 0
    prefix_sum = 0
    sum_map = defaultdict(int)
    sum_map[0] = 1  # To handle subarrays starting from index 0

    for i, char in enumerate(s):
        if char.isdigit():
            prefix_sum += int(char)
        else:
            prefix_sum = 0  # Reset if non-digit character is encountered

        # Check if (current_sum - length) exists in the map
        # current_sum - length = previous_sum => current_sum - previous_sum = length
        for length in range(1, i + 1):
            if (prefix_sum - length) in sum_map:
                count += sum_map[prefix_sum - length]

        sum_map[prefix_sum] += 1

    return count

check(count_substrings_with_sum_equal_to_length)