def check(candidate):
    assert candidate([5,7,10],3,1) == "ODD"
    assert candidate([2,3],2,3) == "EVEN"
    assert candidate([1,2,3],3,1) == "ODD"


def is_last_element_even_or_odd(arr, p):
    # Perform the operation p times
    for _ in range(p):
        # Example operation: reverse the array
        arr = arr[::-1]
    
    # Check if the last element is even or odd
    last_element = arr[-1]
    if last_element % 2 == 0:
        return "even"
    else:
        return "odd"

check(is_last_element_even_or_odd)