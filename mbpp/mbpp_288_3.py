def check(candidate):
    assert candidate([ 1, 6, 4, 5 ], 4, 7) == 2
    assert candidate([1, 3, 8, 12, 12], 5, 13) == 3
    assert candidate([2, 3, 4, 5], 4, 6) == 1


def count_self_inverse_elements(arr, p):
    count = 0
    for num in arr:
        if num % p == 0:
            continue
        try:
            inverse = pow(num, p-2, p)
            if inverse == num:
                count += 1
        except:
            pass
    return count

check(count_self_inverse_elements)