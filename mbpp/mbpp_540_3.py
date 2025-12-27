def check(candidate):
    assert candidate([1,1,2,2,7,8,4,5,1,4],10) == 2
    assert candidate([1,7,9,2,3,3,1,3,3],9) == 3
    assert candidate([1,2,1,2],4) == 0


def frequency_difference(arr):
    from collections import Counter
    
    if not arr:
        return 0
    
    freq = Counter(arr)
    max_freq = max(freq.values())
    min_freq = min(freq.values())
    
    return max_freq - min_freq

check(frequency_difference)