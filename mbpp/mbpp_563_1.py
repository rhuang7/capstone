def check(candidate):
    assert candidate('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
    assert candidate('"python","program","language"')==['python','program','language']
    assert candidate('"red","blue","green","yellow"')==['red','blue','green','yellow']


def extract_values(s):
    import re
    return re.findall(r'"(.*?)"', s)

check(extract_values)