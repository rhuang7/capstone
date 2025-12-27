def check(candidate):
    assert candidate( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
    assert candidate( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
    assert candidate( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')]


def generate_color_combinations(colors, count):
    from itertools import combinations_with_replacement
    
    return list(combinations_with_replacement(colors, count))

check(generate_color_combinations)