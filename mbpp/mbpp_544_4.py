def check(candidate):
    assert candidate([('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]) == '1 4 6 5 8 2 9 1 10'
    assert candidate([('2', '3', '4'), ('6', '9'), ('3', '2'), ('2', '11')]) == '2 3 4 6 9 3 2 2 11'
    assert candidate([('14', '21', '9'), ('24', '19'), ('12', '29'), ('23', '17')]) == '14 21 9 24 19 12 29 23 17'


def flatten_tuple_list_to_string(tuple_list):
    return ','.join(map(str, tuple_list))

check(flatten_tuple_list_to_string)