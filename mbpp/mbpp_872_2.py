def check(candidate):
    assert candidate([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True
    assert candidate([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True
    assert candidate([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False


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