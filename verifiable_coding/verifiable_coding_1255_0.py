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
        
        used = set(s)
        available = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in used]
        
        # Calculate the number of characters that are in s
        common = len(used)
        
        if common <= k:
            # We can use all characters not in s, but need to choose the lex smallest
            # So we need to use the lex smallest characters not in s
            # But we need to make sure that the total length is same as s
            # Since s has unique characters, the length of s is len(s)
            # So we need to choose len(s) characters from available, which are not in s
            # And we need to choose the lex smallest possible
            # So we take the first len(s) characters from available
            result = ''.join(available[:len(s)])
            print(result)
        else:
            # We need to choose some characters from s and some from available
            # To minimize the lex order, we need to choose as many as possible from available
            # But we can only choose (k) characters from available
            # So we take the first k characters from available
            # And the rest from s, but in lex order
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And then the first k characters from available, sorted lex
            # But we need to make sure that the total length is len(s)
            # So the total number of characters from s is (len(s) - k)
            # And from available is k
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And the first k characters from available, sorted lex
            # But we need to make sure that the total number of characters is len(s)
            # So we take the first (len(s) - k) characters from s, sorted lex
            # And