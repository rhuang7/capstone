def check(candidate):
    assert candidate(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
    assert candidate(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)))== [25.5, -18.0, 3.75]
    assert candidate( ((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40)))==[305.0, 342.5, 270.0, 232.5]


def average_of_tuple_of_tuples(tuples_data):
    total = 0
    count = 0
    for inner_tuple in tuples_data:
        for num in inner_tuple:
            total += num
            count += 1
    if count == 0:
        return 0.0
    return total / count

check(average_of_tuple_of_tuples)