def check(candidate):
    assert candidate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[[10, 20], [30, 56, 25], [33], [40]] 
    assert candidate(["a", "b", "a", "c", "c"] )==["a", "b", "c"]
    assert candidate([1, 3, 5, 6, 3, 5, 6, 1] )==[1, 3, 5, 6]


def remove_duplicates(list_of_lists):
    seen = set()
    result = []
    for sublist in list_of_lists:
        frozen_sublist = frozenset(sublist)
        if frozen_sublist not in seen:
            seen.add(frozen_sublist)
            result.append(sublist)
    return result

check(remove_duplicates)