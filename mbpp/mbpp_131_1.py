def check(candidate):
    assert candidate("Python") == "Python"
    assert candidate("USA") == "ASU"
    assert candidate("ab") == "ab"


def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            left += 1
        elif s[right] in vowels:
            right -= 1
        else:
            left += 1
            right -= 1
    return ''.join(s_list)

check(reverse_vowels)