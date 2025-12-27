def check(candidate):
    assert candidate("python")==(6,0)
    assert candidate("program")==(7,0)
    assert candidate("python3.0")==(6,2)


def count_digits_letters(s):
    digits = 0
    letters = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    return digits, letters

check(count_digits_letters)