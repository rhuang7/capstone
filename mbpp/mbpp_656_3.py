def check(candidate):
    assert candidate([3,2,1],[2,1,3],3) == 0
    assert candidate([1,2,3],[4,5,6],3) == 9
    assert candidate([4,1,8,7],[2,3,6,5],4) == 6


def min_sum_abs_diff(arr1, arr2):
    from collections import Counter
    
    # Count frequencies of elements in both arrays
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    # Calculate the minimum sum of absolute differences
    total = 0
    for num in count1:
        if num in count2:
            total += abs(num - num) * count1[num] * count2[num]
        else:
            total += abs(num - 0) * count1[num] * count2.get(0, 0)
    for num in count2:
        if num not in count1:
            total += abs(num - 0) * count2[num] * count1.get(0, 0)
    return total

check(min_sum_abs_diff)