def check(candidate):
    assert candidate((('333', '33'), ('1416', '55')))==((333, 33), (1416, 55))
    assert candidate((('999', '99'), ('1000', '500')))==((999, 99), (1000, 500))
    assert candidate((('666', '66'), ('1500', '555')))==((666, 66), (1500, 555))


def tuple_str_to_int(input_tuple):
    return tuple(int(s) for s in input_tuple)

check(tuple_str_to_int)