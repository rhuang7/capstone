def check(candidate):
    assert candidate([10,20,30,40,40,40,70,80,99],40,100)==6
    assert candidate(['a','b','c','d','e','f'],'a','e')==5
    assert candidate([7,8,9,15,17,19,45],15,20)==3


def count_elements_in_range(lst, lower, upper):
    return sum(1 for x in lst if lower <= x <= upper)

check(count_elements_in_range)