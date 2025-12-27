def check(candidate):
    assert candidate(75)==246.25
    assert candidate(265)==1442.75
    assert candidate(100)==327.5


def calculate_electricity_bill(units):
    # Base charge for the first 100 units
    base_charge = 200
    # Rate per unit after the first 100 units
    rate_per_unit = 5
    
    if units <= 100:
        return units * rate_per_unit
    else:
        return base_charge + (units - 100) * rate_per_unit

check(calculate_electricity_bill)