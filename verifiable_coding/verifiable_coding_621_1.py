import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        words = data[idx:idx + n]
        idx += n
        
        # Find the minimum length of the words
        min_len = min(len(word) for word in words)
        
        # Generate all possible substrings of the shortest word
        candidates = set()
        for i in range(len(words[0])):
            for j in range(i + 1, len(words[0]) + 1):
                substr = words[0][i:j]
                candidates.add(substr)
        
        # Check which substrings are present in all words
        valid = []
        for cand in sorted(candidates):
            found = True
            for word in words:
                if cand not in word:
                    found = False
                    break
            if found:
                valid.append(cand)
        
        # Output the smallest valid substring
        print(valid[0] if valid else "")

if __name__ == '__main__':
    solve()