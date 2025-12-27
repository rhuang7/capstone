def check(candidate):
    assert candidate(10,20)==200
    assert candidate(5,10)==50
    assert candidate(4,8)==32


def multiply(a, b):
    result = 0
    # Iterate b times and add a to the result
    for _ in range(abs(b)):
        result += a
    # Handle negative numbers
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return -result
    return result

check(multiply)