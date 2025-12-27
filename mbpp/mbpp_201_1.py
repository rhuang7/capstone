def check(candidate):
    assert candidate(['one','one','one']) == True
    assert candidate(['one','Two','Three']) == False
    assert candidate(['bigdata','python','Django']) == False


def all_elements_same(lst):
    return all(x == lst[0] for x in lst)

check(all_elements_same)