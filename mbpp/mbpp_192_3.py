def check(candidate):
    assert candidate('thishasboth29') == True
    assert candidate('python') == False
    assert candidate ('string') == False


def has_letter_and_number(s):
    has_letter = any(char.isalpha() for char in s)
    has_number = any(char.isdigit() for char in s)
    return has_letter and has_number

check(has_letter_and_number)