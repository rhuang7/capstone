def check(candidate):
    assert candidate([1,2,3,1,2,3,12,4,2]) ==  2
    assert candidate([1,2,6,7,0,1,0,1,0]) == 1,0
    assert candidate([1,2,3,1,2,4,1]) == 1


def most_frequent_item(lst):
    from collections import Counter
    counts = Counter(lst)
    return max(counts, key=counts.get)

check(most_frequent_item)