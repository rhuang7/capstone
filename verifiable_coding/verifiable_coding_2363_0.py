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
        s = list(map(int, data[idx:idx + n]))
        idx += n
        
        s.sort()
        min_diff = float('inf')
        
        for i in range(n - 1):
            # Split after i-th element
            # Team A is first i+1 elements, team B is remaining
            max_a = s[i]
            min_b = s[i + 1]
            diff = abs(max_a - min_b)
            if diff < min_diff:
                min_diff = diff
        
        results.append(str(min_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()