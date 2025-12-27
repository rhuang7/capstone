def check(candidate):
    assert candidate({'physics': 80, 'math': 90, 'chemistry': 86},0)== 'physics'
    assert candidate({'python':10, 'java': 20, 'C++':30},2)== 'C++'
    assert candidate({'program':15,'computer':45},1)== 'computer'


def get_element_by_index(d, index):
    return d.get(index)

check(get_element_by_index)