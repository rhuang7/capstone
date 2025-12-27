def check(candidate):
    assert candidate(10,15) == 6
    assert candidate(2,4) == 0
    assert candidate(15,16) == 1


def count_hex_numbers(start, end):
    count = 0
    for num in range(start, end + 1):
        if all(c in '0123456789abcdef' for c in hex(num)[2:]):
            count += 1
    return count

check(count_hex_numbers)