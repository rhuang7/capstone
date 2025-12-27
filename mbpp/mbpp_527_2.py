def check(candidate):
    assert candidate([1, 5, 7, -1, 5], 5, 6) == 3
    assert candidate([1, 5, 7, -1], 4, 6) == 2
    assert candidate([1, 1, 1, 1], 4, 2) == 6


def find_pairs_with_sum(arr, target):
    seen = set()
    pairs = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return list(pairs)

check(find_pairs_with_sum)