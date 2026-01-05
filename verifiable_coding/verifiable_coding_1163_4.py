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
        min_so_far = float('inf')
        
        for goal in g:
            if goal > min_so_far:
                max_diff = max(max_diff, goal - min_so_far)
            else:
                min_so_far = goal
        
        if max_diff < 0:
            results.append("UNFIT")
        else:
            results.append(str(max_diff))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()