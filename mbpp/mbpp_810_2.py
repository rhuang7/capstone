def check(candidate):
    assert candidate(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 
    assert candidate(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 
    assert candidate(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']


def repeat_elements_by_count(elements):
    result = []
    for element in elements:
        result.extend([element] * elements.count(element))
    return result

check(repeat_elements_by_count)