def check(candidate):
    assert candidate(["bcda", "abce", "cbda", "cbea", "adcb"],"abcd")==['bcda', 'cbda', 'adcb']
    assert candidate(["recitals"," python"], "articles" )==["recitals"]
    assert candidate([" keep"," abcdef"," xyz"]," peek")==[" keep"]


def find_anagrams(input_string, string_list):
    return list(filter(lambda s: sorted(input_string) == sorted(s), string_list))

check(find_anagrams)