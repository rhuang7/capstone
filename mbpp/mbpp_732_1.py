def check(candidate):
    assert candidate('Python language, Programming language.')==('Python:language::Programming:language:')
    assert candidate('a b c,d e f')==('a:b:c:d:e:f')
    assert candidate('ram reshma,ram rahim')==('ram:reshma:ram:rahim')


def replace_punctuation_with_colon(text):
    return text.replace(' ', ':').replace(',', ':').replace('.', ':')

check(replace_punctuation_with_colon)