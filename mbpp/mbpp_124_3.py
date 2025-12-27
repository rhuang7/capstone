def check(candidate):
    assert candidate(0,1j)==1.5707963267948966 
    assert candidate(2,1j)==0.4636476090008061
    assert candidate(0,2j)==1.5707963267948966


def angle_of_complex(number):
    import math
    return math.atan2(number.imag, number.real)

check(angle_of_complex)