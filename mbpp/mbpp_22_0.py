def check(candidate):
    assert candidate(([1, 2, 3, 4, 4, 5]))==4
    assert candidate([1, 2, 3, 4])==-1
    assert candidate([1, 1, 2, 3, 3, 2, 2])==1


def find_first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

check(find_first_duplicate)