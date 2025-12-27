def check(candidate):
    assert candidate("paper","title") == True
    assert candidate("ab","ba") == True
    assert candidate("ab","aa") == False


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    char_map = {}
    used_chars = set()
    
    for char_s, char_t in zip(s, t):
        if char_s in char_map:
            if char_map[char_s] != char_t:
                return False
        else:
            if char_t in used_chars:
                return False
            char_map[char_s] = char_t
            used_chars.add(char_t)
    
    return True

check(is_isomorphic)