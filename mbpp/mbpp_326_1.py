def check(candidate):
    assert candidate(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
    assert candidate(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
    assert candidate(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'


def most_frequent_word(strings):
    from collections import Counter
    
    word_counts = Counter()
    for s in strings:
        words = s.split()
        word_counts.update(words)
    
    most_common = word_counts.most_common(1)
    return most_common[0][0] if most_common else ""

check(most_frequent_word)