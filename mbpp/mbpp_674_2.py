def check(candidate):
    assert candidate("Python Exercises Practice Solution Exercises")==("Python Exercises Practice Solution")
    assert candidate("Python Exercises Practice Solution Python")==("Python Exercises Practice Solution")
    assert candidate("Python Exercises Practice Solution Practice")==("Python Exercises Practice Solution")


from collections import OrderedDict

def remove_duplicate_words(s):
    words = s.split()
    unique_words = list(OrderedDict.fromkeys(words))
    return ' '.join(unique_words)

check(remove_duplicate_words)