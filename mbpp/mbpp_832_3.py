def check(candidate):
    assert candidate('100klh564abc365bg') == 564
    assert candidate('hello300how546mer231') == 546
    assert candidate('its233beenalong343journey234') == 343


import re

def extract_max_numeric_value(s):
    numbers = re.findall(r'\d+', s)
    if not numbers:
        return None
    return max(map(int, numbers))

check(extract_max_numeric_value)