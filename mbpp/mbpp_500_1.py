def check(candidate):
    assert candidate(['hello','there','have','a','rocky','day'] ) == '  hello there have a rocky day'
    assert candidate([ 'Hi', 'there', 'How','are', 'you'] ) == '  Hi there How are you'
    assert candidate([ 'Part', 'of', 'the','journey', 'is', 'end'] ) == '  Part of the journey is end'


def concatenate_list_elements(input_list):
    return ''.join(input_list)

check(concatenate_list_elements)