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
        
        # Process the string
        res = []
        i = 0
        while i < n:
            if s[i] == '0':
                res.append('0')
                i += 1
            else:
                # We can remove '1' or '0' if there is a '0' next
                if i + 1 < n and s[i + 1] == '0':
                    # Prefer to remove '1' to keep '0' for possible future operations
                    res.append('0')
                    i += 2
                else:
                    res.append('1')
                    i += 1
        
        print(''.join(res))
        
if __name__ == '__main__':
    solve()