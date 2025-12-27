def check(candidate):
    assert candidate("PythonProgramLanguage")==['Python','Program','Language']
    assert candidate("PythonProgram")==['Python','Program']
    assert candidate("ProgrammingLanguage")==['Programming','Language']


def split_at_uppercase(s):
    result = []
    i = 0
    while i < len(s):
        if i > 0 and s[i].isupper():
            result.append('')
        result.append(s[i])
        i += 1
    return ''.join(result)

check(split_at_uppercase)