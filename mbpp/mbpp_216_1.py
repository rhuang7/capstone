def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==False
    assert candidate([[2, 3, 1], [4, 5], [6, 8]],[[4, 5], [6, 8]])==True
    assert candidate([['a', 'b'], ['e'], ['c', 'd']],[['g']])==False


def is_subset(nested_list, super_list):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    def is_subset_helper(sub, sup):
        sub_set = set(flatten(sub))
        sup_set = set(flatten(sup))
        return sub_set.issubset(sup_set)

    return is_subset_helper(nested_list, super_list)

check(is_subset)