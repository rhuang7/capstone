import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # We can only remove 1s and 0s in pairs where a 1 is followed by a 0
        # So we can remove all 1s and 0s in pairs, but we need to choose which to remove
        # To get the cleanest string, we want the shortest possible, and if same length, lex smallest
        
        # We can greedily remove 1s and 0s in a way that leaves the lex smallest string
        # We can do this by keeping track of the number of 1s and 0s we can remove
        
        # Let's count the number of 1s and 0s
        count_1 = s.count('1')
        count_0 = s.count('0')
        
        # We can remove at most min(count_1, count_0) pairs
        # But we want to remove as many as possible to get the shortest string
        
        # The cleanest string is the one with the minimum length, and lex smallest
        # So we want to remove as many as possible, but in a way that leaves the lex smallest string
        
        # We can do this by keeping track of the number of 1s and 0s we can remove
        # We can remove as many as possible, but we need to choose which to remove
        
        # We can simulate the process by iterating through the string and keeping track of the number of 1s and 0s we can remove
        
        # Let's simulate the process
        res = []
        i = 0
        remove_1 = 0
        remove_0 = 0
        
        while i < len(s):
            if s[i] == '1':
                if remove_0 > 0:
                    remove_0 -= 1
                else:
                    res.append('1')
            else:
                if remove_1 > 0:
                    remove_1 -= 1
                else:
                    res.append('0')
            i += 1
        
        # Now, we can remove as many as possible, but we need to choose which to remove
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # So we can remove as many 1s as possible, but only if there are 0s to pair with them
        # Or remove as many 0s as possible, but only if there are 1s to pair with them
        
        # We can do this by counting the number of 1s and 0s and then removing the minimum of the two
        # But we need to choose which to remove to get the lex smallest string
        
        # So we can remove as many as possible, but we want to leave the lex smallest string
        
        # So we can remove as many as possible, but we need to choose which to remove
        # We can remove as many 1s as possible, but only if there are 0s to pair with them
        # Or remove as many 0s as possible, but only if there are 1s to pair with them
        
        # So we can remove as many as possible, but we want to leave the lex smallest string
        
        # So we can remove as many as possible, but we want to leave the lex smallest string
        
        # So we can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the lex smallest string
        
        # We can remove as many as possible, but we want to leave the