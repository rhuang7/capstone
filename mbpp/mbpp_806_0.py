def check(candidate):
    assert candidate('GeMKSForGERksISBESt') == 5
    assert candidate('PrECIOusMOVemENTSYT') == 6
    assert candidate('GooGLEFluTTER') == 4


def max_uppercase_run(s):
    if not s:
        return 0
    
    max_run = 0
    current_run = 0
    
    for char in s:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    
    return max_run

check(max_uppercase_run)