def check(candidate):
    assert candidate(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert candidate(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert candidate(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')


def create_tuple_from_string_and_list(s, lst):
    return tuple(s + lst)

check(create_tuple_from_string_and_list)