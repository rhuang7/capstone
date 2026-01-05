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
        n = int(data[idx])
        idx += 1
        strings = []
        for _ in range(n):
            s = data[idx]
            idx += 1
            strings.append(s)
        
        # Find the minimum possible LCS
        # The minimum LCS is 0 if there is at least one string with no 'a' and another with no 'b'
        has_a = any('a' in s for s in strings)
        has_b = any('b' in s for s in strings)
        
        if not has_a or not has_b:
            results.append(0)
            continue
        
        # Otherwise, the minimum LCS is the minimum number of 'a's or 'b's in any string
        min_count = min(len(s) for s in strings)
        results.append(min_count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()