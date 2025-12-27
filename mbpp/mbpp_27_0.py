def check(candidate):
    assert candidate(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
    assert candidate(['28Jan','12Jan','11Jan']) == ['Jan','Jan','Jan']
    assert candidate(['wonder1','wonder2','wonder3']) == ['wonder','wonder','wonder']


def remove_digits(strings):
    return [s.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '') for s in strings]

check(remove_digits)