def check(candidate):
    assert candidate(1,2) == 1
    assert candidate(23,56) == 6
    assert candidate(123,256) == 7


def digit_distance(a, b):
    # Convert integers to strings to iterate over each digit
    a_str = str(a)
    b_str = str(b)
    
    # Ensure both numbers have the same length by padding with leading zeros
    max_length = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_length)
    b_str = b_str.zfill(max_length)
    
    # Calculate the sum of absolute differences of each corresponding digit
    distance = 0
    for digit_a, digit_b in zip(a_str, b_str):
        distance += abs(int(digit_a) - int(digit_b))
    
    return distance

check(digit_distance)