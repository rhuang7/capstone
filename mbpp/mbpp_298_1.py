def check(candidate):
    assert candidate( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==[[12], [7, 11], [1, 5, 8]]
    assert candidate([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]])==[[], []]
    assert candidate(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']])==[['john'], ['john'], ['john'], []]


def find_nested_elements(nested_list, target_list):
    result = []
    for sublist in nested_list:
        for item in sublist:
            if item in target_list:
                result.append(item)
    return result

check(find_nested_elements)