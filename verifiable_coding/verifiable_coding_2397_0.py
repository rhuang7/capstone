import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        forbidden = set()
        for _ in range(n):
            s = data[idx]
            forbidden.add(s)
            idx += 1
        
        # Generate all binary strings of length m
        all_strs = []
        for i in range(2 ** m):
            binary = bin(i)[2:].zfill(m)
            if binary not in forbidden:
                all_strs.append(binary)
        
        k = len(all_strs)
        median_idx = (k - 1) // 2
        results.append(all_strs[median_idx])
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()