def check(candidate):
    assert candidate(12)==61
    assert candidate(15)==73
    assert candidate(24)==109


def calculate_dog_age(human_years):
    if human_years < 0:
        return "Invalid input: Human years cannot be negative."
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + (human_years - 2) * 4

check(calculate_dog_age)