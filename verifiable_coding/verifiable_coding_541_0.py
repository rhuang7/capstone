import sys

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
        
        color_count = {}
        max_height = 0
        
        for i in range(N):
            color = C[i]
            if color not in color_count:
                color_count[color] = 0
            color_count[color] += 1
        
        for color in color_count:
            count = color_count[color]
            if count % 2 == 0:
                max_height = max(max_height, count // 2)
            else:
                max_height = max(max_height, (count - 1) // 2)
        
        results.append(str(max_height))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()