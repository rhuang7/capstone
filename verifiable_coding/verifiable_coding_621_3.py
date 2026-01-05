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
        
        # Generate all possible substrings of the first word
        substrings = set()
        for i in range(len(words[0])):
            for j in range(i + 1, len(words[0]) + 1):
                substr = words[0][i:j]
                substrings.add(substr)
        
        # Check which substrings are present in all words
        common_substrings = []
        for sub in substrings:
            if all(sub in word for word in words):
                common_substrings.append(sub)
        
        # Sort by length (descending) and then lexicographically (ascending)
        common_substrings.sort(key=lambda x: (-len(x), x))
        
        # Output the longest (and lex smallest in case of tie)
        print(common_substrings[0])

if __name__ == '__main__':
    solve()