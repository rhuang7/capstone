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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = 0
        for num in arr:
            # Calculate weight of the number
            weight = ((num - 1) % 6) + 1
            total += weight
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()