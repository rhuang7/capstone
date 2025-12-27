def check(candidate):
    assert candidate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])==[[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]
    assert candidate([[1,2],[2,3],[3,4]])==[[2,1],[3,2],[4,3]]
    assert candidate([[10,20],[30,40]])==[[20,10],[40,30]]


def reverse_lists(input_list):
    return [lst[::-1] for lst in input_list]

check(reverse_lists)