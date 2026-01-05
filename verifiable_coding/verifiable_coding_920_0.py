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
        
        # To minimize awkwardness, boys and girls should be placed alternately
        # Start with 'b' if there are more boys, else start with 'g'
        start = 'b' if boys >= girls else 'g'
        
        res = 0
        b_pos = 0
        g_pos = 0
        
        for j in range(len(s)):
            if j % 2 == 0:
                if start == 'b':
                    res += b_pos
                    b_pos += 1
                else:
                    res += g_pos
                    g_pos += 1
            else:
                if start == 'b':
                    res += g_pos
                    g_pos += 1
                else:
                    res += b_pos
                    b_pos += 1
        
        results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()