import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        boys = s.count('b')
        girls = len(s) - boys
        
        # To minimize the awkwardness, we should alternate 'b' and 'g' as much as possible
        # Start with 'b' if there are more boys, else start with 'g'
        start_with_b = boys >= girls
        
        res = 0
        pos = 0
        for c in s:
            if c == 'b' and start_with_b:
                res += pos
                start_with_b = False
            elif c == 'g' and not start_with_b:
                res += pos
                start_with_b = True
            pos += 1
        
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()