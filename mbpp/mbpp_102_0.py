def check(candidate):
    assert candidate('python_program')=='PythonProgram'
    assert candidate('python_language')==('PythonLanguage')
    assert candidate('programming_language')==('ProgrammingLanguage')


def snake_to_camel(s):
    parts = s.split('_')
    if not parts:
        return s
    return parts[0] + ''.join(part.title() for part in parts[1:])

check(snake_to_camel)