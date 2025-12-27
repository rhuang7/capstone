def check(candidate):
    assert candidate("1101","1110") == 1
    assert candidate("111","000") == "Not Possible"
    assert candidate("111","110") == "Not Possible"


def min_swaps_to_convert(s1, s2):
    # Count the number of differing characters
    diff = sum(1 for a, b in zip(s1, s2) if a != b)
    
    # If the number of differing characters is odd, it's impossible to convert
    if diff % 2 != 0:
        return -1
    
    # The minimum number of swaps is half the number of differing characters
    return diff // 2

check(min_swaps_to_convert)