def check(candidate):
    assert candidate(10)==16796
    assert candidate(9)==4862
    assert candidate(7)==429


def catalan_number(n):
    if n < 0:
        return 0
    catalan = 1
    for i in range(1, n + 1):
        catalan = catalan * (n + i) // i
    return catalan

check(catalan_number)