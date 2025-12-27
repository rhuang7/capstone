def check(candidate):
    assert candidate([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2])==2
    assert candidate([1, 3,5, 7,1, 3,13, 15, 17,5, 7,9,1, 11])==1
    assert candidate([1, 2, 3,2, 4, 5,1, 1, 1])==1


def most_frequent_item(lst):
    from collections import Counter
    counts = Counter(lst)
    return max(counts, key=counts.get)

check(most_frequent_item)