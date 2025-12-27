def check(candidate):
    assert candidate("Python") == 'Python'
    assert candidate("PythonProgrammingExamples") == 'Python Programming Examples'
    assert candidate("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'


import re

def add_spaces_between_capital_words(text):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)

check(add_spaces_between_capital_words)