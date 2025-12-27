def check(candidate):
    assert candidate("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
    assert candidate("Please handle the situation carefuly") == '28-36: carefuly'
    assert candidate("Complete the task quickly") == '18-25: quickly'


import re

def find_adverbs(sentence):
    # Regular expression to find adverbs
    # An adverb typically ends with 'ly' and may have other adverbial markers
    adverb_pattern = r'\b\w+ly\b'
    adverbs = re.findall(adverb_pattern, sentence)
    # Find positions of each adverb
    positions = []
    for adverb in adverbs:
        start = sentence.find(adverb)
        positions.append((start, start + len(adverb)))
    return adverbs, positions

check(find_adverbs)