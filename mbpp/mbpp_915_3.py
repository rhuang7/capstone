def check(candidate):
    assert candidate([-1, 2, -3, 5, 7, 8, 9, -10])==[2, 5, 7, 8, 9, -10, -3, -1]
    assert candidate([10,15,14,13,-18,12,-20])==[10, 12, 13, 14, 15, -20, -18]
    assert candidate([-20,20,-10,10,-30,30])==[10, 20, 30, -30, -20, -10]


def rearrange_array(arr):
    return list(map(lambda x: x, sorted(arr, key=lambda num: num if num > 0 else float('inf'))))

check(rearrange_array)