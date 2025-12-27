def check(candidate):
    assert candidate("AB3454D") =="Odd"
    assert candidate("ABC") == "Even"
    assert candidate("AAD") == "Odd"


def is_hex_even(hex_number):
    # Convert hexadecimal to integer
    decimal_value = int(hex_number, 16)
    # Check if the decimal value is even
    return decimal_value % 2 == 0

check(is_hex_even)