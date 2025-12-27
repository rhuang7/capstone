def check(candidate):
    assert candidate(4,2)==10.392304845413264
    assert candidate(5,7)==4.639421805988064
    assert candidate(9,1)==105.2220865598093


def largest_triangle_in_ellipse():
    import math
    
    def area_of_triangle(a, b, c):
        return 0.5 * a * b * c
    
    def largest_triangle():
        # The largest triangle that can be inscribed in an ellipse
        # has vertices at (a, 0), (-a, 0), (0, b) where a and b are semi-axes
        # of the ellipse
        a = 2  # semi-major axis
        b = 1  # semi-minor axis
        return area_of_triangle(a, b, math.sqrt(a**2 + b**2))
    
    return largest_triangle()

check(largest_triangle_in_ellipse)