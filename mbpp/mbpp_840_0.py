def check(candidate):
    assert candidate(2,0,-1) == "Yes"
    assert candidate(1,-5,6) == "No"
    assert candidate(2,0,2) == "Yes"


def are_roots_opposite_equal(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    
    # Check if discriminant is zero (roots are equal)
    if discriminant == 0:
        return False  # Roots are equal but not opposite in sign
    
    # Check if roots are opposite in sign
    # Product of roots is c/a, so if c/a is negative, roots are opposite in sign
    if (c / a) < 0:
        return True
    else:
        return False

check(are_roots_opposite_equal)