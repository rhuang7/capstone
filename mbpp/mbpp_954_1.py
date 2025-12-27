def check(candidate):
    assert candidate(1500,1200)==300
    assert candidate(100,200)==None
    assert candidate(2000,5000)==None


def calculate_profit(amount):
    if amount > 0:
        return amount * 0.1  # Assuming 10% profit rate
    else:
        return None

check(calculate_profit)