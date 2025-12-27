def check(candidate):
    assert candidate("pythonz.")==('Found a match!')
    assert candidate("xyz.")==('Found a match!')
    assert candidate("  lang  .")==('Not matched!')


def find_words_with_z(words):
    return [word for word in words if 'z' in word]

check(find_words_with_z)