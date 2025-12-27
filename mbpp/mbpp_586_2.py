def check(candidate):
    assert candidate([12,10,5,6,52,36],6,2) == [5,6,52,36,12,10]
    assert candidate([1,2,3,4],4,1) == [2,3,4,1]
    assert candidate([0,1,2,3,4,5,6,7],8,3) == [3,4,5,6,7,0,1,2]


def rotate_array(arr):
    if not arr:
        return arr
    return arr[1:] + [arr[0]]

check(rotate_array)