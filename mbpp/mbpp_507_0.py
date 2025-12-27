def check(candidate):
    assert candidate(['red', 'green', 'blue', 'white', 'black', 'orange'],['white', 'orange'])==['red', 'green', 'blue', 'black']
    assert candidate(['red', 'green', 'blue', 'white', 'black', 'orange'],['black', 'orange'])==['red', 'green', 'blue', 'white']
    assert candidate(['red', 'green', 'blue', 'white', 'black', 'orange'],['blue', 'white'])==['red', 'green', 'black', 'orange']


def remove_specific_words(word_list, words_to_remove):
    return [word for word in word_list if word not in words_to_remove]

check(remove_specific_words)