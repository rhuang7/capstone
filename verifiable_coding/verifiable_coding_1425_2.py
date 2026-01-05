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
        L1 = data[idx]
        L2 = data[idx+1]
        L3 = data[idx+2]
        N = int(data[idx+3])
        idx += 4
        
        # Convert binary strings to integer
        L = int(L1 + L2 * N + L3, 2)
        
        # Calculate the number of accesses
        count = 0
        while L > 0:
            count += 1
            L = L & (L + 1)
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()