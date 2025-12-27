def check(candidate):
    assert candidate(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black'] 
    assert candidate(['python', 'java'] ,'program')==['program', 'python', 'program', 'java'] 
    assert candidate(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad'] 


def insert_before_each(lst, element):
    return [element + x for x in lst]

check(insert_before_each)