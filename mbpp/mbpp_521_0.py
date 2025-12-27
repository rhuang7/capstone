def check(candidate):
    assert candidate(6,8,12)==True
    assert candidate(6,6,12)==False
    assert candidate(6,15,20)==True


def is_scalene_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Not a valid triangle")
        return
    if a != b and b != c and c != a:
        print("Yes, it's a scalene triangle")
    else:
        print("No, it's not a scalene triangle")

check(is_scalene_triangle)