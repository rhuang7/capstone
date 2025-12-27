def check(candidate):
    assert candidate('GoogleAssistant') == 'google_assistant'
    assert candidate('ChromeCast') == 'chrome_cast'
    assert candidate('QuadCore') == 'quad_core'


import re

def camel_to_snake(camel_str):
    return re.sub('(?<!^)(?=(?:[A-Z]))', '_', camel_str).lower()

check(camel_to_snake)