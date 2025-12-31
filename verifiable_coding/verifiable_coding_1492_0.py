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
        # The minimum LCS is 0 if there's at least one 'a' and one 'b' in all strings
        # Because the hidden omen can be a string with only 'a's or only 'b's
        # So check if there's at least one 'a' and one 'b' in all strings
        has_a = all('a' in s for s in strings)
        has_b = all('b' in s for s in strings)
        
        if has_a and has_b:
            results.append(0)
        else:
            # The minimum LCS is the minimum count of 'a' or 'b' across all strings
            min_count = min(min(s.count('a') for s in strings), min(s.count('b') for s in strings))
            results.append(min_count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()