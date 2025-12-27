def check(candidate):
    assert candidate(["julia", "best", "tseb", "for", "ailuj"])== '2'
    assert candidate(["geeks", "best", "for", "skeeg"]) == '1'
    assert candidate(["makes", "best", "sekam", "for", "rof"]) == '2' 


def count_reverse_pairs(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i] == strings[j][::-1]:
                count += 1
    return count

check(count_reverse_pairs)