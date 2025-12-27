def check(candidate):
    assert candidate(["red","green","black","orange"],["red","pink","green","white","black"])==True
    assert candidate(["red","pink","green","white","black"],["white","orange","pink","black"])==False
    assert candidate(["red","green","black","orange"],["red","pink","green","white","black"])==True


def are_common_elements_in_order(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    if not common:
        return False
    common_list = list(common)
    for i in range(len(common_list)):
        if list1.index(common_list[i]) != list2.index(common_list[i]):
            return False
    return True

check(are_common_elements_in_order)