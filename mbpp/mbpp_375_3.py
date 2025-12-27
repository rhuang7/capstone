def check(candidate):
    assert candidate(4722,10)==4720
    assert candidate(1111,5)==1110
    assert candidate(219,2)==218


def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple

check(round_to_multiple)