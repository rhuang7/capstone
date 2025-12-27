def check(candidate):
    assert candidate("abcc","c") == 2
    assert candidate("ababca","a") == 3
    assert candidate("mnmm0pm","m") == 4


def count_character_occurrence(s, char):
    return s.count(char)

check(count_character_occurrence)