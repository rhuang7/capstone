def check(candidate):
    assert candidate(50,60,70)==True
    assert candidate(90,45,45)==True
    assert candidate(150,30,70)==False


def is_valid_triangle(angles):
    if not isinstance(angles, list):
        return False
    if len(angles) != 3:
        return False
    for angle in angles:
        if not isinstance(angle, (int, float)) or angle <= 0:
            return False
    if sum(angles) != 180:
        return False
    return all(0 < angle < 180 for angle in angles)

check(is_valid_triangle)