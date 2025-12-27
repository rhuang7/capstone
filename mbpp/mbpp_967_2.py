def check(candidate):
    assert candidate("SEEquoiaL") == 'accepted'
    assert candidate('program') == "not accepted"
    assert candidate('fine') == "not accepted"


def contains_all_vowels(s):
    vowels = set('aeiou')
    return vowels.issubset(s.lower())

check(contains_all_vowels)