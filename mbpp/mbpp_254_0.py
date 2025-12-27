def check(candidate):
    assert candidate("python programe")==['ame']
    assert candidate("python programe language")==['ame','anguage']
    assert candidate("assert statement")==['assert', 'atement']


def find_words_starting_with_a_or_e(text):
    import re
    return re.findall(r'\b[a Ae][^ae\s]*\b', text)

check(find_words_starting_with_a_or_e)