def check(candidate):
    assert candidate(1,2,3) == "Obtuse-angled Triangle"
    assert candidate(2,2,2) == "Acute-angled Triangle"
    assert candidate(1,0,1) == "Right-angled Triangle"


def triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    
    # Check for equilateral triangle
    if a == b == c:
        return "equilateral"
    
    # Check for isosceles triangle
    if a == b or a == c or b == c:
        return "isosceles"
    
    # Otherwise, it's a scalene triangle
    return "scalene"

check(triangle_type)