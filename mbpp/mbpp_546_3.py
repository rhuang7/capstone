def check(candidate):
    assert candidate("hello world",'l')==10
    assert candidate("language",'g')==7
    assert candidate("little",'y')==None


def find_last_occurrence(s, char):
    return s.rfind(char)

check(find_last_occurrence)