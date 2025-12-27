def check(candidate):
    assert candidate('The person is most value tet', 3) == 'person is most value'
    assert candidate('If you told me about this ok', 4) == 'If you me about ok'
    assert candidate('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'


def remove_k_length_words(s, k):
    words = s.split()
    filtered_words = [word for word in words if len(word) != k]
    return ' '.join(filtered_words)

check(remove_k_length_words)