def check(candidate):
    assert candidate("abcac",'a') == 4
    assert candidate("abca",'c') == 2
    assert candidate("aba",'a') == 7


def count_char_in_repeated_string(s, char, num_repeats):
    # Create a repeated string
    repeated_string = s * num_repeats
    # Count occurrences of the character
    return repeated_string.count(char)

check(count_char_in_repeated_string)