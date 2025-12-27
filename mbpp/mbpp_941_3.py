def check(candidate):
    assert candidate([10,20,30,(10,20),40])==3
    assert candidate([10,(20,30),(10,20),40])==1
    assert candidate([(10,(20,30,(10,20),40))])==0


def count_elements_until_tuple(lst):
    count = 0
    for item in lst:
        if isinstance(item, tuple):
            break
        count += 1
    return count

check(count_elements_until_tuple)