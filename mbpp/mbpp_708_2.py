def check(candidate):
    assert candidate('python program') == ['python','program']
    assert candidate('Data Analysis') ==['Data','Analysis']
    assert candidate('Hadoop Training') == ['Hadoop','Training']


def string_to_list(s):
    return list(s)

check(string_to_list)