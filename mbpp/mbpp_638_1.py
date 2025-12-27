def check(candidate):
    assert candidate(120,35)==40
    assert candidate(40,70)==86
    assert candidate(10,100)==116


def calculate_wind_chill(wind_speed, temperature):
    if temperature > 10 or wind_speed < 3:
        return temperature
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

check(calculate_wind_chill)