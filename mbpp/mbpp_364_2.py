def check(candidate):
    assert candidate("0001010111") == 2
    assert candidate("001") == 1
    assert candidate("010111011") == 2 


def count_alternating_flips(s):
    # Count flips needed to make the string alternate starting with '0'
    flips0 = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != '0':
            flips0 += 1
        elif i % 2 == 1 and s[i] != '1':
            flips0 += 1
    
    # Count flips needed to make the string alternate starting with '1'
    flips1 = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != '1':
            flips1 += 1
        elif i % 2 == 1 and s[i] != '0':
            flips1 += 1
    
    return min(flips0, flips1)

check(count_alternating_flips)