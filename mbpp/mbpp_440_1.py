def check(candidate):
    assert candidate("clearly!! we can see the sky")==(0, 7, 'clearly')
    assert candidate("seriously!! there are many roses")==(0, 9, 'seriously')
    assert candidate("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')


def find_adverbs(sentence):
    import re
    adverbs = []
    # Regular expression to find adverbs (words ending in 'ly')
    pattern = r'\b\w+ly\b'
    matches = re.finditer(pattern, sentence)
    for match in matches:
        adverb = match.group()
        start = match.start()
        end = match.end()
        adverbs.append((adverb, start, end))
    return adverbs

check(find_adverbs)