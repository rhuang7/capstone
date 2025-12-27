def check(candidate):
    assert candidate({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
    assert candidate({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
    assert candidate({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False


def all_values_same(d):
    if not d:
        return True
    first_value = next(iter(d.values()))
    return all(value == first_value for value in d.values())

check(all_values_same)