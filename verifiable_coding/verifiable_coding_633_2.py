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
        max_height = -1
        for _ in range(N):
            h = int(data[idx])
            idx += 1
            if h > max_height:
                max_height = h
        results.append(str(max_height))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()