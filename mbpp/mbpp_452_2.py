def check(candidate):
    assert candidate(1500,1200)==None
    assert candidate(100,200)==100
    assert candidate(2000,5000)==3000


def calculate_loss(amount):
    if amount < 0:
        return amount
    else:
        return None

check(calculate_loss)