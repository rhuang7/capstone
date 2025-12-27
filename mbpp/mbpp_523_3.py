def check(candidate):
    assert candidate('python')==['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.']
    assert candidate('123python')==['String must have 1 upper case character.']
    assert candidate('123Python')==['Valid string.']


def check_string_requirements(s):
    has_capital = lambda x: any(c.isupper() for c in x)
    has_lowercase = lambda x: any(c.islower() for c in x)
    has_number = lambda x: any(c.isdigit() for c in x)
    has_length = lambda x: len(x) == 8  # Assuming the required length is 8 as per common use case

    return has_capital(s) and has_lowercase(s) and has_number(s) and has_length(s)

check(check_string_requirements)