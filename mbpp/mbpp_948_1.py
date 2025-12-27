def check(candidate):
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==('e')
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-4)==('u')
    assert candidate(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-3)==('r')


def get_tuple_item(t, index):
    return t[index] if 0 <= index < len(t) else None

check(get_tuple_item)