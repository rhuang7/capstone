def check(candidate):
    assert candidate(60,50,90)==False
    assert candidate(45,75,60)==True
    assert candidate(30,50,100)==True


def is_triangle_valid(a, b, c):
    return a + b > c and a + c > b and b + c > a

check(is_triangle_valid)