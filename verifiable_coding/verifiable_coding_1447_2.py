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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        from collections import defaultdict
        count = defaultdict(int)
        freq = {}
        valid = True
        
        for num in A:
            count[num] += 1
            if count[num] > 1:
                valid = False
        
        if not valid:
            results.append("NO")
            continue
        
        freq = {}
        for num in A:
            if num in freq:
                valid = False
                break
            freq[num] = count[num]
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()