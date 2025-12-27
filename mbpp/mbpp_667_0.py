def check(candidate):
    assert candidate('corner','AaEeIiOoUu') == 2
    assert candidate('valid','AaEeIiOoUu') == 2
    assert candidate('true','AaEeIiOoUu') ==2


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

check(count_vowels)