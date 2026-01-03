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
        
        # Create a list of colors
        colors = []
        for color, cnt in freq:
            colors.extend([color] * cnt)
        
        # Try to rearrange
        res = []
        for i in range(N):
            if i % 2 == 0:
                res.append(colors[i // 2])
            else:
                res.append(colors[i // 2])
        
        # Check if it's valid
        valid = True
        for i in range(N):
            if res[i] == a[i]:
                valid = False
                break
        
        if valid:
            results.append("Yes")
            results.append(" ".join(map(str, res)))
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()