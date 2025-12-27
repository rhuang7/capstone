def check(candidate):
    assert candidate(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
    assert candidate(["Python Programming","Java Programming"])==('Python','Programming')
    assert candidate(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')


def find_p_word_pairs(words):
    p_words = [word for word in words if word.startswith('p')]
    return list(zip(p_words, p_words[1:]))

check(find_p_word_pairs)