def check(candidate):
    assert candidate(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
    assert candidate(["apples", "ape", "april"], 3) == 'ap'
    assert candidate(["teens", "teenager", "teenmar"], 3) == 'teen'


def longest_common_prefix(strings):
    if not strings:
        return ""
    
    # Take the first string as the initial prefix
    prefix = strings[0]
    
    for string in strings[1:]:
        # Update the prefix by comparing with current string
        prefix = prefix[:len(string)]
        if not prefix:
            return ""
    
    return prefix

check(longest_common_prefix)