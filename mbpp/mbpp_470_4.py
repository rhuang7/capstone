def check(candidate):
    assert candidate((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert candidate((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert candidate((3, 7, 9, 10, 12)) == (10, 16, 19, 22)


def pairwise_addition(tuples_list):
    if not tuples_list:
        return []
    result = []
    for i in range(len(tuples_list[0])):
        total = 0
        for tup in tuples_list:
            if i < len(tup):
                total += tup[i]
        result.append(total)
    return result

check(pairwise_addition)