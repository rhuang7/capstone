def check(candidate):
    assert candidate("machine learning","machine") == True
    assert candidate("easy","fun") == False
    assert candidate("python language","code") == False


def word_in_sentence(word, sentence):
    return word in sentence.split()

check(word_in_sentence)