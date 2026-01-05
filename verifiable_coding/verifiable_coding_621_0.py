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
        candidates = set()
        for i in range(len(words[0])):
            for j in range(i+1, len(words[0])+1):
                substr = words[0][i:j]
                if len(substr) <= min_len:
                    candidates.add(substr)
        
        # Check which candidates are present in all words
        valid = []
        for cand in sorted(candidates):
            all_contain = True
            for word in words:
                if cand not in word:
                    all_contain = False
                    break
            if all_contain:
                valid.append(cand)
        
        # Output the smallest valid candidate
        print(valid[0])

if __name__ == '__main__':
    solve()