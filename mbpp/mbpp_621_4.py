def check(candidate):
    assert candidate(["MSM", "234", "is", "98", "123", "best", "4"] , 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']
    assert candidate(["Dart", "356", "is", "88", "169", "Super", "6"] , 12) == ['Dart', '368', 'is', '100', '181', 'Super', '18']
    assert candidate(["Flutter", "451", "is", "44", "96", "Magnificent", "12"] , 33) == ['Flutter', '484', 'is', '77', '129', 'Magnificent', '45']


def increment_numeric_values(strings, k):
    result = []
    for s in strings:
        new_str = ""
        for char in s:
            if char.isdigit():
                new_str += str(int(char) + k)
            else:
                new_str += char
        result.append(new_str)
    return result

check(increment_numeric_values)