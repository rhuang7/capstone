def check(candidate):
    assert candidate({1:'python',2:'java'})==[1,2]
    assert candidate({10:'red',20:'blue',30:'black'})==[10,20,30]
    assert candidate({27:'language',39:'java',44:'little'})==[27,39,44]


def get_keys_as_list(d):
    return list(d.keys())

check(get_keys_as_list)