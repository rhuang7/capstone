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
        # The minimum LCS is the minimum number of 'a's or 'b's that are common in all strings
        # We count the minimum count of 'a's and 'b's across all strings
        min_a = min(s.count('a') for s in strings)
        min_b = min(s.count('b') for s in strings)
        results.append(min(min_a, min_b))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()