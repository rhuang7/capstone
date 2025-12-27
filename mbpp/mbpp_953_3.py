def check(candidate):
    assert candidate([1, 2, 3, 4],4) == 1
    assert candidate([5, 6, 9, 3, 4, 3, 4],7) == 2
    assert candidate([1, 2, 3 ],3) == 1


def min_subsets_with_distinct_elements(elements):
    from collections import Counter
    
    # Count the frequency of each element
    freq = Counter(elements)
    
    # The minimum number of subsets is the maximum frequency of any element
    return max(freq.values(), default=0)

check(min_subsets_with_distinct_elements)