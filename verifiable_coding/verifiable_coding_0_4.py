import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        words = []
        for i in range(n):
            word = data[idx]
            idx += 1
            words.append(word)
        
        # Build a graph where each node is a word, and edges represent possible transitions
        # We'll use a dictionary to map last character to a list of words that end with that character
        # Also, we'll track the first character of each word
        first_char = {}
        last_char = {}
        for i, word in enumerate(words):
            first_char[i] = word[0]
            last_char[i] = word[-1]
        
        # Build adjacency list
        adj = collections.defaultdict(list)
        for i in range(n):
            c = last_char[i]
            adj[c].append(i)
        
        # We need to find an Eulerian path in this graph, where each edge represents a transition
        # The Eulerian path must visit each node exactly once (since each word is used once)
        # So we need to find a path that uses each node once, possibly reversing some words
        
        # We'll try to find a valid path by checking for possible reversals
        # We'll use a DFS approach to find a valid path, trying to reverse words when necessary
        
        # Try to find a valid path
        visited = [False] * n
        path = []
        reversed_words = set()
        
        def dfs(u, prev_last_char):
            visited[u] = True
            path.append(u)
            if len(path) == n:
                # Found a valid path
                return True
            
            # Try to find a next word that starts with the last character of the current word
            # If not found, try to reverse the current word and see if it helps
            current_last_char = last_char[u]
            next_words = []
            for v in range(n):
                if not visited[v] and first_char[v] == current_last_char:
                    next_words.append(v)
            
            if next_words:
                # Try to proceed with the next word
                for v in next_words:
                    if dfs(v, last_char[u]):
                        return True
                # Backtrack
                path.pop()
                visited[u] = False
                return False
            
            # No next word found, try to reverse the current word
            reversed_word = words[u][::-1]
            if reversed_word not in words:
                # Check if the reversed word can be used
                reversed_last_char = reversed_word[-1]
                next_words = []
                for v in range(n):
                    if not visited[v] and first_char[v] == reversed_last_char:
                        next_words.append(v)
                
                if next_words:
                    # Try to proceed with the reversed word
                    # Mark this word as reversed
                    reversed_words.add(u)
                    # Update the last character of this word
                    last_char[u] = reversed_last_char
                    # Try to proceed
                    for v in next_words:
                        if dfs(v, reversed_last_char):
                            return True
                    # Backtrack
                    path.pop()
                    visited[u] = False
                    reversed_words.remove(u)
                    return False
            
            # No valid path found
            return False
        
        # Try to find a path starting with each word
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                path = [i]
                if dfs(i, last_char[i]):
                    # Found a valid path
                    # Now check if all words are unique (after possible reversals)
                    # Since we reversed some words, we need to check if any of them are the same
                    # But since the original words are unique, and we only reverse some, the reversed words must be unique
                    # So we can proceed
                    # Now, collect the reversed words
                    res = []
                    for j in range(n):
                        if j in reversed_words:
                            res.append(j + 1)
                    results.append(str(len(res)))
                    results.append(' '.join(map(str, res)))
                    break
                else:
                    # No valid path found
                    results.append("-1")
        
    # Output the results
    print('\n'.join(results))