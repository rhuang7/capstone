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
        for substr in substrings:
            if all(substr in word for word in words):
                common_substrings.append(substr)
        
        # If there are common substrings, choose the smallest lexicographically
        if common_substrings:
            print(min(common_substrings))
        else:
            print("")

if __name__ == '__main__':
    solve()