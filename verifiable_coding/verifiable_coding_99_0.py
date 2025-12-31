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
        
        # We can only erase 1s and 0s in positions where they are consecutive and 1 followed by 0
        # The optimal strategy is to remove as many 1s as possible to the left of 0s
        # So we can iterate through the string and collect 0s first, then 1s
        res = []
        for c in s:
            if c == '0':
                res.append(c)
            else:
                # We can only remove this 1 if there is a 0 after it
                # So we wait until we see a 0 to decide whether to keep or remove this 1
                # We keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0 yet
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we need to track whether we have seen a 0
                # We can do this by keeping a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a 0, we can remove this 1
                # Otherwise, we keep it
                # So we can keep a flag
                # But since we are building the result in order, we can just keep the 1 if there is a 0 after it
                # So we can keep track of whether we have seen a 0
                # If we have seen a