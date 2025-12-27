def check(candidate):
    assert candidate(["red", "black", "white", "green", "orange"],"ack")==True
    assert candidate(["red", "black", "white", "green", "orange"],"abc")==False
    assert candidate(["red", "black", "white", "green", "orange"],"ange")==True


def is_substring_present(strings, substring):
    return any(substring in s for s in strings)

check(is_substring_present)