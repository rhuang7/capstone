def check(candidate):
    assert candidate(["red","green","green"], ["a", "b", "b"])==True 
    assert candidate(["red","green","greenn"], ["a","b","b"])==False 
    assert candidate(["red","green","greenn"], ["a","b"])==False 


def follows_pattern(sequence, patterns):
    if not patterns:
        return False
    
    for pattern in patterns:
        if len(pattern) != len(sequence):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] != sequence[i] and pattern[i] != '*':
                return False
    
    return True

check(follows_pattern)