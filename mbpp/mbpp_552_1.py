def check(candidate):
    assert candidate([0,2,4,6,8,10]) == "Linear Sequence"
    assert candidate([1,2,3]) == "Linear Sequence"
    assert candidate([1,5,2]) == "Non Linear Sequence"


def is_linear(sequence):
    if not sequence:
        return False  # Empty sequence is not linear
    
    # Check if all elements are the same
    if all(x == sequence[0] for x in sequence):
        return True
    
    # Check if the sequence is strictly increasing or decreasing
    increasing = all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1))
    decreasing = all(sequence[i] > sequence[i+1] for i in range(len(sequence)-1))
    
    return increasing or decreasing

check(is_linear)