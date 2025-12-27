def check(candidate):
    assert candidate(2,0,2) == "Yes"
    assert candidate(2,-5,2) == "Yes"
    assert candidate(1,2,3) == "No"


def are_reciprocal_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    
    # Check if discriminant is negative (no real roots)
    if discriminant < 0:
        return False
    
    # Calculate the roots
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    
    # Check if roots are reciprocal of each other
    # Avoid division by zero by checking if product is 1
    if root1 * root2 == 1:
        return True
    else:
        return False

check(are_reciprocal_roots)