def check(candidate):
    assert candidate([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
    assert candidate([-1, 1, -1, 8]) == [-1]
    assert candidate([1, 2, 3, 1, 2,]) == [1, 2]


def print_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    for dup in duplicates:
        print(dup)

check(print_duplicates)