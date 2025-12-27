def check(candidate):
    assert candidate([0,1,2,3],0,3) == 4
    assert candidate([0,1,2,6,9],0,4) == 3
    assert candidate([2,3,5,8,9],0,4) == 0


def smallest_missing(arr):
    # Create a set of the array for O(1) lookups
    num_set = set(arr)
    # Start checking from 0
    missing = 0
    while True:
        if missing not in num_set:
            return missing
        missing += 1

check(smallest_missing)