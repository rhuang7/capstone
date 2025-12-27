def check(candidate):
    assert candidate(2,3,1,10) == 5
    assert candidate(3,6,4,20) == 11
    assert candidate(5,10,4,20) == 16


def find_nth_non_multiple(n, k):
    count = 0
    num = 1
    while True:
        if num % k != 0:
            count += 1
            if count == n:
                return num
        num += 1

check(find_nth_non_multiple)