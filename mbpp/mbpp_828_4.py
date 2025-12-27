def check(candidate):
    assert candidate("abc!@#123")==(3,3,3)
    assert candidate("dgsuy@#$%&1255")==(5,4,5)
    assert candidate("fjdsif627348#%$^&")==(6,6,5)


def count_characters(s):
    alphabets = 0
    digits = 0
    special = 0
    for char in s:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    return alphabets, digits, special

check(count_characters)