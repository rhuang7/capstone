def check(candidate):
    assert candidate([(6, 9), (15, 34), (48, 70)], 2, 100) == [(2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)]
    assert candidate([(7, 2), (15, 19), (38, 50)], 5, 60) == [(5, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 60)]
    assert candidate([(7, 2), (15, 19), (38, 50)], 1, 52) == [(1, 7), (2, 52), (2, 15), (19, 52), (19, 38), (50, 52)]


def extract_missing_ranges(numbers, start, end):
    numbers.sort()
    missing = []
    i = 0
    while i < len(numbers):
        current = numbers[i]
        if current > start:
            missing.append((start, current - 1))
        while i + 1 < len(numbers) and numbers[i + 1] == current + 1:
            i += 1
        i += 1
    if numbers[-1] < end:
        missing.append((numbers[-1] + 1, end))
    return missing

check(extract_missing_ranges)