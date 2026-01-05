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
        
        # Find transition point in sorted array
        # All 0s come before all 1s
        # So find the first occurrence of 1
        transition = 0
        for num in arr:
            if num == 1:
                transition = arr.index(1)
                break
        
        results.append(str(transition))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()