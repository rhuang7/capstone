def check(candidate):
    assert candidate(10,20)==100
    assert candidate(10,5)==25
    assert candidate(4,2)==4


def area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

check(area_of_rhombus)