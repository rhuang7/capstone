def check(candidate):
    assert candidate("0011","1111") == 1
    assert candidate("00011","01001") == 2
    assert candidate("111","111") == 0


def min_swaps_to_equal(s1, s2):
    swaps = 0
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            # Find the next character in s1 that matches s2[i]
            j = i + 1
            while j < len(s1):
                if s1[j] == s2[i]:
                    # Swap s1[i] and s1[j]
                    swaps += 1
                    # Update s1 to reflect the swap
                    s1 = s1[:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:]
                    break
                j += 1
            else:
                # No matching character found, strings cannot be equal
                return -1
        i += 1
    return swaps

check(min_swaps_to_equal)