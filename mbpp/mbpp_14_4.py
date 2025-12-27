def check(candidate):
    assert candidate(10,8,6) == 240
    assert candidate(3,2,2) == 6
    assert candidate(1,2,1) == 1


def triangular_prism_volume(base, height, length):
    """
    Calculate the volume of a triangular prism.
    
    The volume is calculated as (base * height * length) / 2.
    """
    return (base * height * length) / 2

check(triangular_prism_volume)