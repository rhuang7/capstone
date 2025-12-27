def check(candidate):
    assert candidate(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    assert candidate((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
    assert candidate(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))


def get_tuple_size(t):
    return len(t)

check(get_tuple_size)