import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        if n == 2:
            results.append(' '.join(map(str, [p[1], p[0]])))
            continue
        
        # For n >= 3, we can reverse the permutation
        p_reversed = p[::-1]
        if p_reversed != p:
            results.append(' '.join(map(str, p_reversed)))
        else:
            # If reversed is same as original (like [1,2,3,4] reversed is [4,3,2,1], which is different)
            # So we can swap first two elements
            results.append(' '.join(map(str, [p[1], p[0]] + p[2:])))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()