def check(candidate):
    assert candidate([10, 20, 30, 40])==[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]
    assert candidate(['X', 'Y', 'Z'])==[[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']]
    assert candidate([1,2,3])==[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]


def generate_sublists(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublists.append(lst[i:j])
    return sublists

check(generate_sublists)