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
        # The minimum possible LCS is 0 if there is at least one 'a' and one 'b' in all strings
        # Because the hidden omen can be a string with only 'a's or only 'b's, making LCS 0
        has_a = all('a' in s for s in strings)
        has_b = all('b' in s for s in strings)
        
        if not has_a and not has_b:
            # All strings are made of only 'a's or only 'b's
            # The LCS is the minimum number of 'a's or 'b's in all strings
            min_a = min(len(s) for s in strings if 'a' in s)
            min_b = min(len(s) for s in strings if 'b' in s)
            results.append(min(min_a, min_b))
        elif not has_a or not has_b:
            # At least one string has both 'a' and 'b'
            # The hidden omen can be all 'a's or all 'b's, making LCS 0
            results.append(0)
        else:
            # The hidden omen can be all 'a's or all 'b's, making LCS 0
            results.append(0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()