def check(candidate):
    assert candidate('PythonProgram')==('python_program')
    assert candidate('pythonLanguage')==('python_language')
    assert candidate('ProgrammingLanguage')==('programming_language')


def camel_to_snake(camel_str):
    snake_str = ''
    for char in camel_str:
        if char.isupper():
            snake_str += '_' + char.lower()
        else:
            snake_str += char
    return snake_str.rstrip('_')

check(camel_to_snake)