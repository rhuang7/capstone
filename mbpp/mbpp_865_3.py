def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7],3)==[3, 6, 9, 12, 15, 18, 21]
    assert candidate([1, 2, 3, 4, 5, 6, 7],4)==[4, 8, 12, 16, 20, 24, 28]
    assert candidate([1, 2, 3, 4, 5, 6, 7],10)==[10, 20, 30, 40, 50, 60, 70]


def print_list_n_times(n, lst):
    for _ in range(n):
        print(list(map(lambda x: x, lst)))

check(print_list_n_times)