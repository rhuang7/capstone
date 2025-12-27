def check(candidate):
    assert candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[100,90]
    assert candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[100,90,80,70,60]
    assert candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[100,90,80]


def get_n_largest_items(data, n):
    if not data or n <= 0:
        return []
    return sorted(data, reverse=True)[:n]

check(get_n_largest_items)