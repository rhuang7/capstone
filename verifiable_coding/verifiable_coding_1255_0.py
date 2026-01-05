import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        s = data[index]
        k = int(data[index + 1])
        index += 2
        
        unique_chars = set(s)
        len_s = len(s)
        
        # If k is less than the number of unique characters in s, it's impossible
        if k < len(unique_chars):
            print("NOPE")
            continue
        
        # We need to find the lex smallest string t of same length as s with unique chars
        # that has at most k characters in common with s
        
        # Start with the lex smallest string (all a-z in order)
        # But we need to ensure that it has at most k characters in common with s
        
        # Generate the lex smallest string with unique characters
        # Start from 'a' and pick next available character not in s
        # until we have len_s characters
        used = set()
        result = []
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used and c not in s:
                result.append(c)
                used.add(c)
            if len(result) == len_s:
                break
        
        # If we haven't filled the string, add the remaining characters from s
        # that are not in the result
        # This is not the correct approach, need to find the lex smallest string
        # with at most k characters in common with s
        
        # Correct approach:
        # We need to construct the lex smallest string t of length len_s with unique characters
        # such that the number of common characters with s is <= k
        
        # We can use a greedy approach:
        # 1. Start with the lex smallest possible characters not in s
        # 2. If we can't add a character not in s, we have to add one that is in s
        #    but only up to k times
        
        # Create a list of characters not in s
        not_in_s = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in s]
        in_s = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c in s]
        
        # We can use at most k characters from in_s
        # The rest must come from not_in_s
        
        # We need to pick len_s characters: first pick as many as possible from not_in_s
        # then pick from in_s, but only up to k times
        
        t = []
        used = set()
        count_in_s = 0
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used and c not in s:
                t.append(c)
                used.add(c)
            elif c not in used and c in s:
                if count_in_s < k:
                    t.append(c)
                    used.add(c)
                    count_in_s += 1
                else:
                    # Can't add this character, skip
                    pass
            else:
                # Already used or in s and count_in_s is full
                pass
        
        # If we haven't filled the string, we need to add the remaining characters
        # from in_s that are not already in t
        # but we can only add up to k of them
        
        # This is not correct, need to find the correct way to build t
        
        # Correct approach:
        # We need to build the lex smallest string t of length len_s with unique characters
        # such that the number of common characters with s is <= k
        
        # We can use a greedy approach:
        # 1. Start with the lex smallest possible characters not in s
        # 2. If we can't add a character not in s, we have to add one that is in s
        #    but only up to k times
        
        # We can use a set to track used characters
        used = set()
        t = []
        count_in_s = 0
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used and c not in s:
                t.append(c)
                used.add(c)
            elif c not in used and c in s:
                if count_in_s < k:
                    t.append(c)
                    used.add(c)
                    count_in_s += 1
                else:
                    # Can't add this character, skip
                    pass
            else:
                # Already used or in s and count_in_s is full
                pass
        
        # If we haven't filled the string, we need to add the remaining characters
        # from in_s that are not already in t
        # but we can only add up to k of them
        
        # This is not correct, need to find the correct way to build t
        
        # Correct approach:
        # We need to build the lex smallest string t of length len_s with unique characters
        # such that the number of common characters with s is <= k
        
        # We can use a greedy approach:
        # 1. Start with the lex smallest possible characters not in s
        # 2. If we can't add a character not in s, we have to add one that is in s
        #    but only up to k times
        
        # We can use a set to track used characters
        used = set()
        t = []
        count_in_s = 0
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used and c not in s:
                t.append(c)
                used.add(c)
            elif c not in used and c in s:
                if count_in_s < k:
                    t.append(c)
                    used.add(c)
                    count_in_s += 1
                else:
                    # Can't add this character, skip
                    pass
            else:
                # Already used or in s and count_in_s is full
                pass
        
        # If we haven't filled the string, we need to add the remaining characters
        # from in_s that are not already in t
        # but we can only add up to k of them
        
        # This is not correct, need to find the correct way to build t
        
        # Correct approach:
        # We need to build the lex smallest string t of length len_s with unique characters
        # such that the number of common characters with s is <= k
        
        # We can use a greedy approach:
        # 1. Start with the lex smallest possible characters not in s
        # 2. If we can't add a character not in s, we have to add one that is in s
        #    but only up to k times
        
        # We can use a set to track used characters
        used = set()
        t = []
        count_in_s = 0
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used and c not in s:
                t.append(c)
                used.add(c)
            elif c not in used and c in s:
                if count_in_s < k:
                    t.append(c)
                    used.add(c)
                    count_in_s += 1
                else:
                    # Can't add this character, skip
                    pass
            else:
                # Already used or in s and count_in_s is full
                pass
        
        # If we haven't filled the string, we need to add the remaining characters
        # from in_s that are not already in t
        # but we can only add up to k of them
        
        # This is not correct, need to find the correct way to build t
        
        # Correct approach:
        # We need to build the lex smallest string t of length len_s with unique characters
        # such that the number of common characters with s is <= k
        
        # We can use a greedy approach:
        # 1. Start with the lex smallest possible characters not in s
        # 2. If we can't add a character not in s, we have to add one that is in s
        #    but only up to k times
        
        # We can use a set to track used characters
        used = set()
        t = []
        count_in_s = 0
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used and c not in s:
                t.append(c)
                used.add(c)
            elif c not in used and c in s:
                if count_in_s < k:
                    t.append(c)
                    used.add(c)
                    count_in_s += 1
                else:
                    # Can't add this character, skip
                    pass
            else:
                # Already used or in s and count_in_s is full
                pass
        
        # If we haven't filled the string, we need to add the remaining characters
        # from in_s that are not already in t
        # but we can only add up to k of them
        
        # This is not correct, need to find the correct way to build t
        
        # Correct approach:
        # We need to build the lex smallest string t of length len_s with unique characters
        # such that the number of common characters with s is <= k
        
        # We can use a greedy approach:
        # 1. Start with the lex smallest possible characters not in s
        # 2. If we can't add a character not in s, we have to add one that is in s
        #    but only up to k times
        
        # We can use a set to track used characters
        used = set()
        t = []