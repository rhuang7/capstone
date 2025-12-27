def check(candidate):
    assert candidate("hello","l") == "heo"
    assert candidate("abcda","a") == "bcd"
    assert candidate("PHP","P") == "H"


def remove_first_last_occurrence(s, char):
    first = s.find(char)
    last = s.rfind(char)
    if first == -1 or last == -1:
        return s
    return s[:first] + s[first+1:last] + s[last+1:]

check(remove_first_last_occurrence)