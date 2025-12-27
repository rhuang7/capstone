def check(candidate):
    assert candidate([1, 2, 2, 3], 4) == 3
    assert candidate([1, 9, 3, 10, 4, 20, 2], 7) == 4
    assert candidate([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11) == 5


def longest_consecutive_subsequence_length(nums):
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

check(longest_consecutive_subsequence_length)