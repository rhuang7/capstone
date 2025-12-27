def check(candidate):
    assert candidate(4,3)== [3,6,9,12]
    assert candidate(2,5)== [5,10]
    assert candidate(9,2)== [2,4,6,8,10,12,14,16,18]


def find_multiples(n, m):
    return [n * i for i in range(1, m + 1)]

check(find_multiples)