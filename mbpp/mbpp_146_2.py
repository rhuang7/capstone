def check(candidate):
    assert candidate("python")==112
    assert candidate("Program")==80
    assert candidate("Language")==76


def find_ascii_value_of_total_characters(s):
    return sum(ord(char) for char in s)

check(find_ascii_value_of_total_characters)