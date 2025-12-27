def check(candidate):
    assert candidate([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert candidate([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert candidate([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]


def find_common_first_element(tuples_list):
    if not tuples_list:
        return None
    common_element = tuples_list[0][0]
    for tup in tuples_list[1:]:
        if tup[0] != common_element:
            return None
    return common_element

check(find_common_first_element)