def check(candidate):
    assert candidate(5)==[{},{},{},{},{}]
    assert candidate(6)==[{},{},{},{},{},{}]
    assert candidate(7)==[{},{},{},{},{},{},{}]


def create_empty_dict_list(n):
    return [{} for _ in range(n)]

check(create_empty_dict_list)