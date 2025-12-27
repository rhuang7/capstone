def check(candidate):
    assert candidate( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == '[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]'
    assert candidate( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == '[(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]'
    assert candidate( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == '[(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]'


def convert_to_float(lst):
    return [float(x) for x in lst if isinstance(x, (int, float))]

check(convert_to_float)