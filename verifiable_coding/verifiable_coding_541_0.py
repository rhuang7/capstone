import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_height = 0
        color_count = collections.defaultdict(int)
        left = 0
        
        for right in range(N):
            color = C[right]
            color_count[color] += 1
            
            while right - left + 1 > 2 * max_height + 1:
                left_color = C[left]
                color_count[left_color] -= 1
                left += 1
            
            if right - left + 1 == 2 * max_height + 1:
                for c in color_count:
                    if color_count[c] % 2 == 0:
                        pass
                    else:
                        max_height += 1
                        break
        
        results.append(str(max_height))
    
    print('\n'.join(results))