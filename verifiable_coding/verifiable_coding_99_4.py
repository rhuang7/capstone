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
        
        # We can only erase 1's and 0's in adjacent positions where s[i] is 1 and s[i+1] is 0
        # The optimal strategy is to remove as many 1's as possible to make the string as short as possible
        # But we need to ensure that the resulting string is lexicographically smallest
        
        # We'll process the string from left to right, keeping track of the number of 1's we can remove
        # We can remove a 1 when we see a 0, but we need to make sure that we don't remove more 1's than available
        # We'll also track the current string as we build it
        
        res = []
        ones = 0
        
        for c in s:
            if c == '1':
                ones += 1
                res.append('1')
            else:
                # We can remove this 0 and the previous 1 if there are any
                if ones > 0:
                    ones -= 1
                    # We don't add the 0, but we don't add the 1 either
                    # So we just skip this 0 and the previous 1
                else:
                    res.append('0')
        
        # Now, we need to make sure that the resulting string is lexicographically smallest
        # We can do this by removing any extra 1's that are not necessary
        # We'll process the string again from left to right, and if we see a 1 followed by a 0, we can remove the 1
        # But we need to make sure that we don't remove more 1's than necessary
        
        # We'll iterate through the string again and remove any extra 1's
        new_res = []
        i = 0
        while i < len(res):
            if res[i] == '1':
                # Check if there is a 0 after this 1
                j = i + 1
                while j < len(res) and res[j] == '1':
                    j += 1
                if j < len(res) and res[j] == '0':
                    # We can remove this 1
                    i += 1
                else:
                    new_res.append('1')
                    i += 1
            else:
                new_res.append('0')
                i += 1
        
        print(''.join(new_res))

if __name__ == '__main__':
    solve()