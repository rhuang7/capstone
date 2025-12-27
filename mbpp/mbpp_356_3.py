def check(candidate):
    assert candidate(47,89)==44
    assert candidate(45,95)==40
    assert candidate(50,40)==90


def find_third_angle(angle1, angle2):
    return 180 - angle1 - angle2

check(find_third_angle)