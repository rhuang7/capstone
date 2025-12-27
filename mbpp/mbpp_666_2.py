def check(candidate):
    assert candidate("Python",'o')==1
    assert candidate("little",'t')==2
    assert candidate("assert",'s')==2


def count_character_occurrence(s, char):
    return s.count(char)

check(count_character_occurrence)