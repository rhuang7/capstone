def check(candidate):
    assert candidate([{},{},{}])==True
    assert candidate([{1,2},{},{}])==False
    assert candidate({})==True


def are_all_dicts_empty(dicts_list):
    return all(not d for d in dicts_list)

check(are_all_dicts_empty)