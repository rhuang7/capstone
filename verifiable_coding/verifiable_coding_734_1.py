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
        
        # Create a list of colors with their frequencies
        color_list = []
        for color, cnt in freq:
            color_list.extend([color] * cnt)
        
        # Try to rearrange the colors
        res = []
        i = 0
        j = len(color_list) - 1
        while i <= j:
            if i == j:
                res.append(color_list[i])
                break
            if color_list[i] != color_list[j]:
                res.append(color_list[i])
                res.append(color_list[j])
                i += 1
                j -= 1
            else:
                # Swap with the next different color
                found = False
                for k in range(i + 1, len(color_list)):
                    if color_list[k] != color_list[i]:
                        res.append(color_list[k])
                        res.append(color_list[i])
                        color_list[k], color_list[i] = color_list[i], color_list[k]
                        found = True
                        break
                if not found:
                    res.append(color_list[i])
                    res.append(color_list[j])
                    i += 1
                    j -= 1
        
        if len(res) != N:
            results.append("No")
            continue
        
        results.append("Yes")
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))