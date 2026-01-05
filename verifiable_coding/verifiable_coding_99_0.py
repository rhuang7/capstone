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
        # The optimal strategy is to remove as many 1s as possible, but in a way that leaves the lex smallest string
        # We can do this by greedily removing 1s when they are followed by 0s
        
        res = []
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == '1' and s[i + 1] == '0':
                # We can remove either the 1 or the 0, but to get the lex smallest string, we remove the 1
                res.append('0')
                i += 2
            else:
                res.append(s[i])
                i += 1
        
        print(''.join(res))

if __name__ == '__main__':
    solve()