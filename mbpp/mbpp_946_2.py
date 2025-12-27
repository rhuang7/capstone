def check(candidate):
    assert candidate('lkseropewdssafsdfafkpwe',3)==[('s', 4), ('e', 3), ('f', 3)] 
    assert candidate('lkseropewdssafsdfafkpwe',2)==[('s', 4), ('e', 3)]
    assert candidate('lkseropewdssafsdfafkpwe',7)==[('s', 4), ('e', 3), ('f', 3), ('k', 2), ('p', 2), ('w', 2), ('d', 2)]


def most_common_elements(text):
    from collections import Counter
    return Counter(text).most_common()

check(most_common_elements)