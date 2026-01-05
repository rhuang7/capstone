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
        can_rearrange = True
        for color, cnt in freq:
            if cnt > (N + 1) // 2:
                can_rearrange = False
                break
        
        if not can_rearrange:
            results.append("No")
            continue
        
        # Create a list of colors in the order they appear in the original array
        original = a
        # Create a list of colors in the order they appear in the frequency sorted list
        sorted_colors = []
        for color, _ in freq:
            sorted_colors.extend([color] * count[color])
        
        # Try to rearrange
        rearranged = []
        i = 0
        j = 0
        while i < N and j < N:
            if original[i] != sorted_colors[j]:
                rearranged.append(sorted_colors[j])
                j += 1
            else:
                i += 1
        
        if len(rearranged) < N:
            results.append("No")
            continue
        
        results.append("Yes")
        results.append(' '.join(map(str, rearranged)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()