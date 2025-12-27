def check(candidate):
    assert candidate("python")==("pto")
    assert candidate("program")==("porm")
    assert candidate("language")==("lnug")


def remove_even_characters(s):
    return ''.join(char for idx, char in enumerate(s) if idx % 2 == 0)

check(remove_even_characters)