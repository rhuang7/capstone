def check(candidate):
    assert candidate(1)==("I")
    assert candidate(50)==("L")
    assert candidate(4)==("IV")


def int_to_roman(num):
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    res = ''
    for (i, roman) in val:
        while num >= i:
            res += roman
            num -= i
    return res

check(int_to_roman)