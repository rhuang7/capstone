def check(candidate):
    assert candidate([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert candidate([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert candidate([1,2,3,4,5]) == [1, 2, 3, 4, 5]


def remove_duplicates_from_lists(lists):
    seen = set()
    result = []
    for lst in lists:
        unique_lst = []
        for num in lst:
            if num not in seen:
                seen.add(num)
                unique_lst.append(num)
        result.append(unique_lst)
    return result

check(remove_duplicates_from_lists)