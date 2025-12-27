def check(candidate):
    assert candidate(8) == 18
    assert candidate(4) == 2
    assert candidate(1) == 0


def max_volume_given_sum(s):
    if s <= 0:
        return 0
    # For maximum volume, the sides should be as close as possible
    # So we divide the sum into three equal parts
    a = b = c = s // 3
    remainder = s % 3
    if remainder == 1:
        a += 1
    elif remainder == 2:
        a += 1
        b += 1
    return a * b * c

check(max_volume_given_sum)