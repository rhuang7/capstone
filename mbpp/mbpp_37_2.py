def check(candidate):
    assert candidate([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert candidate([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
    assert candidate([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']


def sort_mixed_list(mixed_list):
    return sorted(mixed_list)

check(sort_mixed_list)