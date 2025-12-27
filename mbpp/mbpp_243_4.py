def check(candidate):
    assert candidate([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]) == [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]
    assert candidate([('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]) == [('b', 'ball', 'b', 2), ('a', 'arm', 'ant', 2)]
    assert candidate([(2, 'Mark'), (3, 'Maze'), (2, 'Sara')]) == [(2, 'Mark', 'Sara', 2), (3, 'Maze', 1)]


def sort_by_first_element_occurrence(lst):
    from collections import Counter
    
    # Count occurrences of the first element of each tuple
    count = Counter()
    for t in lst:
        count[t[0]] += 1
    
    # Sort the list based on the occurrence count of the first element
    # Higher occurrence comes first
    lst.sort(key=lambda x: -count[x[0]])
    
    return lst

check(sort_by_first_element_occurrence)