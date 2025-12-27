def check(candidate):
    assert candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20]
    assert candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[10,20,20,40,50]
    assert candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[10,20,20]


def get_n_smallest(data, n):
    if n <= 0:
        return []
    if n >= len(data):
        return data
    return sorted(data)[:n]

check(get_n_smallest)