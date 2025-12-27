def check(candidate):
    assert candidate(90)==5156.620156177409
    assert candidate(60)==3437.746770784939
    assert candidate(120)==6875.493541569878


def radians_to_degrees(radians):
    return radians * 180 / 3.141592653589793

check(radians_to_degrees)