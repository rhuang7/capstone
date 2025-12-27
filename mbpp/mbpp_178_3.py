def check(candidate):
    assert candidate(['language'],'python language')==('Matched!')
    assert candidate(['program'],'python language')==('Not Matched!')
    assert candidate(['python'],'programming language')==('Not Matched!')


def search_literals(text, literals):
    matches = []
    for literal in literals:
        if literal in text:
            matches.append(literal)
    return matches

check(search_literals)