def check(candidate):
    assert candidate(1,3,2) == "Yes"
    assert candidate(1,2,3) == "No"
    assert candidate(1,-5,6) == "No"


def is_root_twice_of_other(a, b, c):
    # Calculate discriminant
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return False  # No real roots
    
    # Calculate roots
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    
    # Check if one root is twice the other
    return abs(root1 - 2 * root2) < 1e-9 or abs(root2 - 2 * root1) < 1e-9

check(is_root_twice_of_other)