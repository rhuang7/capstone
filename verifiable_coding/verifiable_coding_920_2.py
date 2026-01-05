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
        
        # To minimize awkwardness, we should alternate between 'b' and 'g'
        # Starting with 'b' if there are more boys, otherwise start with 'g'
        start_with_b = boys >= girls
        
        res = 0
        b_idx = 0
        g_idx = 0
        
        for pos in range(len(s)):
            if pos % 2 == 0:
                if start_with_b and b_idx < boys:
                    res += g_idx
                    b_idx += 1
                else:
                    res += g_idx
                    g_idx += 1
            else:
                if start_with_b and b_idx < boys:
                    res += g_idx
                    b_idx += 1
                else:
                    res += g_idx
                    g_idx += 1
        
        results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()