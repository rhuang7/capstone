def check(candidate):
    assert candidate([5,9,7,6],4) == 47
    assert candidate([7,3,5],3) == 12
    assert candidate([7,3],2) == 4


def sum_xor_pairs(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            total += (arr[i] ^ arr[j])
    return total

check(sum_xor_pairs)