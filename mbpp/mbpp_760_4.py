def check(candidate):
    assert candidate([1,1,1],3) == 'YES'
    assert candidate([1,2,1,2],4) == 'NO'
    assert candidate([1,2,3,4,5],5) == 'NO'


def has_only_one_distinct_element(arr):
    if not arr:
        return False
    return all(x == arr[0] for x in arr)

check(has_only_one_distinct_element)