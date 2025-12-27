def check(candidate):
    assert candidate([1,1,1,1],4,2) == 6
    assert candidate([1,5,7,-1,5],5,6) == 3
    assert candidate([1,-2,3],3,1) == 1


def count_pairs_with_sum(arr, sum):
    count = 0
    seen = set()
    for num in arr:
        complement = sum - num
        if complement in seen:
            count += 1
        seen.add(num)
    return count

check(count_pairs_with_sum)