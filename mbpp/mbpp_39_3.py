def check(candidate):
    assert candidate("aab")==('aba')
    assert candidate("aabb")==('abab')
    assert candidate("abccdd")==('cdabcd')


def can_rearrange(s):
    from collections import Counter

    count = Counter(s)
    max_char = max(count.values())
    unique_chars = len(count)

    if max_char > (len(s) + 1) // 2:
        return False
    if unique_chars > (len(s) + 1) // 2:
        return False
    return True

check(can_rearrange)