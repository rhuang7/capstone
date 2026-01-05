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
        S = data[idx]
        idx += 1
        n = int(data[idx])
        idx += 1
        arr = set(data[idx:idx + n])
        idx += n
        
        valid = True
        for c in S:
            if c not in arr:
                valid = False
                break
        results.append('1' if valid else '0')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()