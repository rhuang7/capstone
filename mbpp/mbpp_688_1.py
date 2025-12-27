def check(candidate):
    assert candidate(3,4)==5.0
    assert candidate(9,10)==13.45362404707371
    assert candidate(7,9)==11.40175425099138


def length_of_complex_number(complex_num):
    return abs(complex_num)

check(length_of_complex_number)