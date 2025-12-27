def check(candidate):
    assert candidate(6,8,12)==False 
    assert candidate(6,6,12)==True
    assert candidate(6,16,20)==False


def is_isosceles(a, b, c):
    # Check if any two sides are equal
    if a == b or b == c or a == c:
        print("Yes")
    else:
        print("No")

check(is_isosceles)