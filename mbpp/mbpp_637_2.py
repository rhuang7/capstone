def check(candidate):
    assert candidate(1500,1200)==False
    assert candidate(100,100)==True
    assert candidate(2000,5000)==False


def has_no_profit_no_loss(amount):
    return amount == 0

check(has_no_profit_no_loss)