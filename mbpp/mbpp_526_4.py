def check(candidate):
    assert candidate("python") == "PythoN"
    assert candidate("bigdata") == "BigdatA"
    assert candidate("Hadoop") == "HadooP"


def capitalize_first_last_letters(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) < 1:
            result.append(word)
        else:
            result.append(word[0].upper() + word[-1].upper())
    return ' '.join(result)

check(capitalize_first_last_letters)