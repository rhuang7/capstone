def check(candidate):
    assert candidate(['Red', 'Blue', 'Black', 'White', 'Pink'])==[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
    assert candidate(['python'])==[['p', 'y', 't', 'h', 'o', 'n']]
    assert candidate([' red ', 'green',' black', 'blue ',' orange', 'brown'])==[[' ', 'r', 'e', 'd', ' '], ['g', 'r', 'e', 'e', 'n'], [' ', 'b', 'l', 'a', 'c', 'k'], ['b', 'l', 'u', 'e', ' '], [' ', 'o', 'r', 'a', 'n', 'g', 'e'], ['b', 'r', 'o', 'w', 'n']]


def list_strings_with_map(strings):
    return list(map(lambda s: s, strings))

check(list_strings_with_map)