def check(candidate):
    assert candidate("probasscurve", "pros") == 'bacuve'
    assert candidate("digitalindia", "talent") == 'digiidi'
    assert candidate("exoticmiles", "toxic") == 'emles' 


def remove_chars_from_first_string(first_string, second_string):
    return ''.join(char for char in first_string if char not in second_string)

check(remove_chars_from_first_string)