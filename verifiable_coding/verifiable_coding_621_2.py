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
        words = data[idx:idx+n]
        idx += n
        
        # Find the minimum length of the words
        min_len = min(len(word) for word in words)
        
        # Generate all possible substrings of the first word
        substrings = set()
        for i in range(len(words[0])):
            for j in range(i+1, len(words[0])+1):
                substr = words[0][i:j]
                substrings.add(substr)
        
        # Check which substrings are present in all words
        common = set(words[0])
        for word in words[1:]:
            common = common & set(word)
        
        # Find the longest common substring
        candidates = [s for s in substrings if s in common]
        if not candidates:
            print("")
            continue
        
        # Find the longest one, then the lexicographically smallest
        max_len = max(len(s) for s in candidates)
        candidates = [s for s in candidates if len(s) == max_len]
        result = min(candidates)
        print(result)

if __name__ == '__main__':
    solve()