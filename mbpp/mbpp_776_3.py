def check(candidate):
    assert candidate('bestinstareels') == 7
    assert candidate('partofthejourneyistheend') == 12
    assert candidate('amazonprime') == 5


def count_vowel_neighbors(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in range(1, len(s) - 1):
        if s[i-1] in vowels and s[i+1] in vowels:
            count += 1
    return count

check(count_vowel_neighbors)