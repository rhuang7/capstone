def check(candidate):
    assert candidate([('Hello', 'dude'), ('How', 'are'), ('you', '?')], [('Hello', 'dude'), ('How', 'are')]) == [('you', '?')]
    assert candidate([('Part', 'of'), ('the', 'journey'), ('is ', 'end')], [('Journey', 'the'), ('is', 'end')]) == [('Part', 'of'), ('the', 'journey'), ('is ', 'end')]
    assert candidate([('Its', 'been'), ('a', 'long'), ('day', 'without')], [('a', 'long'), ('my', 'friend')]) == [('Its', 'been'), ('day', 'without')]


def remove_matching_tuples(tuple1, tuple2):
    # Convert tuples to sets for efficient element removal
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    # Find the intersection of the two sets
    common_elements = set1 & set2
    
    # Remove common elements from both tuples
    new_tuple1 = tuple(element for element in tuple1 if element not in common_elements)
    new_tuple2 = tuple(element for element in tuple2 if element not in common_elements)
    
    return new_tuple1, new_tuple2

check(remove_matching_tuples)