def check(candidate):
    assert candidate((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)
    assert candidate((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)
    assert candidate((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)


def find_similar_elements(tuple_list1, tuple_list2):
    set1 = set(tuple_list1)
    set2 = set(tuple_list2)
    return list(set1 & set2)

check(find_similar_elements)