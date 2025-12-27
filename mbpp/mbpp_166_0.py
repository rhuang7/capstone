def check(candidate):
    assert candidate([5,4,7,2,1],5) == 4
    assert candidate([7,2,8,1,0,5,11],7) == 9
    assert candidate([1,2,3],3) == 1


def count_even_xor_pairs(nums):
    even_count = 0
    odd_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count * odd_count

check(count_even_xor_pairs)