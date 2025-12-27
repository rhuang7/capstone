def check(candidate):
    assert candidate(1,5,2,5,4,6) == 'Yes'
    assert candidate(1,1,1,4,1,5) == 'No'
    assert candidate(1,1,1,1,1,1) == 'No'


def is_valid_triangle(p1, p2, p3):
    # Calculate the squared distances between the points
    def squared_distance(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    a2 = squared_distance(p1, p2)
    b2 = squared_distance(p2, p3)
    c2 = squared_distance(p3, p1)
    
    # Check triangle inequality theorem (squared to avoid sqrt)
    if (a2 + b2 > c2) and (a2 + c2 > b2) and (b2 + c2 > a2):
        return True
    else:
        return False

check(is_valid_triangle)