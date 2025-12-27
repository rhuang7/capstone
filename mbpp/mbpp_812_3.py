def check(candidate):
    assert candidate("ravipadu Road")==('ravipadu Rd.')
    assert candidate("palnadu Road")==('palnadu Rd.')
    assert candidate("eshwar enclave Road")==('eshwar enclave Rd.')


def abbreviate_road(input_string):
    return input_string.replace('road', 'rd.')

check(abbreviate_road)