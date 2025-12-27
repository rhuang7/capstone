def check(candidate):
    assert candidate(["Python", "Exercises", "Practice", "Solution", "Exercises"])==['Python', 'Exercises', 'Practice', 'Solution']
    assert candidate(["Python", "Exercises", "Practice", "Solution", "Exercises","Java"])==['Python', 'Exercises', 'Practice', 'Solution', 'Java']
    assert candidate(["Python", "Exercises", "Practice", "Solution", "Exercises","C++","C","C++"])==['Python', 'Exercises', 'Practice', 'Solution','C++','C']


def remove_duplicate_words(word_list):
    return list(dict.fromkeys(word_list))

check(remove_duplicate_words)