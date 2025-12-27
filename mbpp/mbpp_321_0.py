def check(candidate):
    assert candidate("111111") == '12345654321'
    assert candidate("1111") == '1234321'
    assert candidate("13333122222") == '123456789101110987654321'


def demlo_number(n):
    if n < 1:
        return ""
    result = ""
    for i in range(n, 0, -1):
        result += str(i) * i
    return result

check(demlo_number)