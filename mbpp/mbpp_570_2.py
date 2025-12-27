def check(candidate):
    assert candidate(['Red color', 'Orange#', 'Green', 'Orange @', "White"],['#', 'color', '@'])==['Red', '', 'Green', 'Orange', 'White']
    assert candidate(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['&', '+', '@'])==['Red', '', 'Green', 'Orange', 'White']
    assert candidate(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['@'])==['Red &', 'Orange+', 'Green', 'Orange', 'White']


def remove_words_with_char(word_list, char):
    return [word for word in word_list if char not in word]

check(remove_words_with_char)