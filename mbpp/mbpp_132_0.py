def check(candidate):
    assert candidate(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
    assert candidate(('p','y','t','h','o','n'))==("python")
    assert candidate(('p','r','o','g','r','a','m'))==("program")


def tuple_to_string(t):
    return ''.join(map(str, t))

check(tuple_to_string)