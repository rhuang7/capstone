def check(candidate):
    assert candidate([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
    assert candidate([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
    assert candidate([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5


def count_same_pairs(list1, list2, list3):
    from collections import Counter
    
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    counter3 = Counter(list3)
    
    common_elements = set(counter1.keys()) & set(counter2.keys()) & set(counter3.keys())
    
    total_pairs = 0
    for element in common_elements:
        count1 = counter1[element]
        count2 = counter2[element]
        count3 = counter3[element]
        total_pairs += min(count1, count2, count3)
    
    return total_pairs

check(count_same_pairs)