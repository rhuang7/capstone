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
        g = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_diff = -1
        min_so_far = g[0]
        for i in range(1, N):
            if g[i] > min_so_far:
                diff = g[i] - min_so_far
                if diff > max_diff:
                    max_diff = diff
            else:
                min_so_far = g[i]
        
        if max_diff > 0:
            results.append(str(max_diff))
        else:
            results.append("UNFIT")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()