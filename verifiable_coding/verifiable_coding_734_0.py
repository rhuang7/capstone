import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        count = collections.Counter(a)
        freq = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Check if it's possible to rearrange
        possible = True
        for color, cnt in freq:
            if cnt > (N + 1) // 2:
                possible = False
                break
        
        if not possible:
            results.append("No")
            continue
        
        # Create a list of colors in the order they appear
        color_list = []
        for color, cnt in freq:
            color_list.extend([color] * cnt)
        
        # Try to rearrange
        res = []
        for i in range(N):
            if i % 2 == 0:
                res.append(color_list[(N - i) // 2])
            else:
                res.append(color_list[(N - i) // 2])
        
        results.append("Yes")
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))