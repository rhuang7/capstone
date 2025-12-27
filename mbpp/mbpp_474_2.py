def check(candidate):
    assert candidate("polygon",'y','l')==("pollgon")
    assert candidate("character",'c','a')==("aharaater")
    assert candidate("python",'l','a')==("python")


def replace_characters(input_string, old_char, new_char):
    return input_string.replace(old_char, new_char)

check(replace_characters)