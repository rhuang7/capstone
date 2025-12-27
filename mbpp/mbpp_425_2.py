def check(candidate):
    assert candidate([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    assert candidate([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
    assert candidate([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1


def count_sublists_with_element(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count

check(count_sublists_with_element)