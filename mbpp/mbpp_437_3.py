def check(candidate):
    assert candidate("python")==("yhn")
    assert candidate("program")==("rga")
    assert candidate("language")==("agae")


def remove_odd_characters(s):
    return ''.join(char for char in s if ord(char) % 2 == 0)

check(remove_odd_characters)