def check(candidate):
    assert candidate("1101","1110") == 1
    assert candidate("1111","0100") == "Not Possible"
    assert candidate("1110000","0001101") == 3


def min_swaps_to_convert(s1, s2):
    # Count the number of differing characters between the two strings
    diff_count = sum(1 for a, b in zip(s1, s2) if a != b)
    
    # If the number of differing characters is even, it's possible to convert
    # Each swap can fix two differing characters
    if diff_count % 2 != 0:
        return -1  # Not possible to convert
    
    # The minimum number of swaps is half the number of differing characters
    return diff_count // 2

check(min_swaps_to_convert)