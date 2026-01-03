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
        
        velocity = 0
        current_velocity = 0
        
        for w in W:
            if current_velocity < w:
                velocity = max(velocity, w - current_velocity + 1)
            current_velocity += 1
        
        results.append(str(velocity))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()