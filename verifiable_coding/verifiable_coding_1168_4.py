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
        s = data[idx]
        idx += 1
        good_chars = data[idx]
        idx += 1
        k = int(data[idx])
        idx += 1
        
        # Map good characters
        good = set()
        for i in range(26):
            if good_chars[i] == '1':
                good.add(chr(ord('a') + i))
        
        # Precompute bad characters
        bad = set()
        for i in range(26):
            if good_chars[i] == '0':
                bad.add(chr(ord('a') + i))
        
        # Count distinct good substrings
        distinct = set()
        
        n = len(s)
        for i in range(n):
            current = []
            bad_count = 0
            for j in range(i, n):
                if s[j] in bad:
                    bad_count += 1
                if bad_count > k:
                    break
                current.append(s[j])
                distinct.add(''.join(current))
        
        results.append(str(len(distinct)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()