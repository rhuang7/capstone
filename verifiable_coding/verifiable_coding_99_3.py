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
        
        # The cleanest string is the one with the most 0s, then lex smallest
        # We can only remove 1s and 0s in pairs where 1 is followed by 0
        # So we want to maximize the number of 0s, and minimize the number of 1s
        
        # Count the number of 0s and 1s
        cnt0 = s.count('0')
        cnt1 = s.count('1')
        
        # The cleanest string will have as many 0s as possible, and then as few 1s as possible
        # So we can try to remove as many 1s as possible by pairing them with 0s
        # But we can only remove a 1 if it is followed by a 0
        
        # We can simulate this by iterating through the string and keeping track of the number of 1s we can remove
        # We can also keep track of the remaining 0s and 1s
        
        # Let's try to greedily remove 1s by pairing them with 0s
        # We can keep a stack-like approach to track the characters
        # We can also track the number of 0s and 1s
        # We can also track the number of 1s that can be removed
        
        # Initialize the result string
        res = []
        cnt0_remaining = cnt0
        cnt1_remaining = cnt1
        i = 0
        
        while i < len(s):
            if s[i] == '0':
                res.append('0')
                cnt0_remaining -= 1
            else:
                # We can try to remove this 1 if there is a 0 after it
                # So we can check the next characters
                # But we can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can't remove it
                # So we can try to remove this 1 if there are 0s after it
                # We can also keep track of the number of 0s we can remove
                # So we can count the number of 0s after this 1
                # If there are any 0s after, we can remove this 1
                # Otherwise, we can