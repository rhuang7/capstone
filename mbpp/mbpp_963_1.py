def check(candidate):
    assert candidate(4,8,2)==("Two solutions",32)
    assert candidate(5,7,9)==("no real solution",-131)
    assert candidate(0,0,9)==("one solution",0)


def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

check(calculate_discriminant)