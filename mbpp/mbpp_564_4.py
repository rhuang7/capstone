def check(candidate):
    assert candidate([1,2,1],3) == 2
    assert candidate([1,1,1,1],4) == 0
    assert candidate([1,2,3,4,5],5) == 10


def count_unequal_pairs(arr):
    if not arr or len(arr) < 2:
        return 0
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] != arr[j]:
                count += 1
    return count

check(count_unequal_pairs)