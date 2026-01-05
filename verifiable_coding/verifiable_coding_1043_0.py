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
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        forgotten = data[idx:idx+N]
        idx += N
        
        phrase_words = []
        
        for _ in range(K):
            L = int(data[idx])
            idx += 1
            phrase_words.extend(data[idx:idx+L])
            idx += L
        
        # Create a set of all words in phrases for fast lookup
        phrase_set = set(phrase_words)
        
        # Determine if each forgotten word is in the phrase set
        output = []
        for word in forgotten:
            if word in phrase_set:
                output.append("YES")
            else:
                output.append("NO")
        
        results.append(" ".join(output))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()