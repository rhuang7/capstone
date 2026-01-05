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
        
        # Create a set to store unique substrings
        unique_substrings = set()
        
        # Precompute which characters are good
        good_set = set()
        for i in range(26):
            if good_chars[i] == '1':
                good_set.add(chr(ord('a') + i))
        
        # Iterate over all possible substrings
        n = len(s)
        for i in range(n):
            bad_count = 0
            substr = ""
            for j in range(i, n):
                substr += s[j]
                if s[j] in good_set:
                    continue
                else:
                    bad_count += 1
                if bad_count > k:
                    break
            if bad_count <= k:
                unique_substrings.add(substr)
        
        results.append(str(len(unique_substrings)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()