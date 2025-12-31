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
        W = list(map(int, data[idx:idx+N]))
        idx += N
        
        vel = 0
        for w in reversed(W):
            if vel < w:
                vel = w
            vel -= 1
        results.append(str(vel))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()