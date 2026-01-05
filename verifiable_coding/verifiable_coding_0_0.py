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
        
        # Create a graph where each node is a word, and edges represent possible transitions
        # We'll use a directed graph where each node is a word, and an edge from A to B exists if B starts with the last character of A
        # We'll also track the last character of each word
        
        # Build the graph
        graph = collections.defaultdict(list)
        last_char = {}
        for i, word in enumerate(words):
            last_char[i] = word[-1]
            graph[word].append(i)
        
        # For each word, we can choose to reverse it or not
        # We need to find a way to arrange all words in a sequence where each word starts with the last character of the previous one
        # We'll try to find a valid sequence with minimal reversals
        
        # We'll use a topological sort approach, but with the possibility of reversing words
        
        # We'll try to build a valid sequence by choosing whether to reverse each word or not
        # We'll use a DFS approach with memoization to find the minimal number of reversals
        
        # We'll try to build a valid sequence by starting with each word and trying to build a chain
        # If we can build a valid sequence, we'll record the number of reversals and the indices of reversed words
        
        # We'll use a memoization dictionary to avoid recomputing the same states
        memo = {}
        
        def dfs(word, last_char, reversed_words, reversed_count):
            # If we've already computed this state, return the result
            state = (word, last_char, tuple(reversed_words))
            if state in memo:
                return memo[state]
            
            # Try to add the current word to the sequence
            # We can choose to reverse it or not
            # If we reverse it, the new last character is the first character of the reversed word
            # If we don't reverse it, the new last character is the original last character
            
            # Check if we can add the current word to the sequence
            # We need to ensure that the current word starts with the last character of the previous word
            # If the current word is not reversed, it starts with the original first character
            # If it is reversed, it starts with the reversed first character
            
            # We can try both options
            # Option 1: do not reverse the word
            if word.startswith(last_char):
                # Try to build the sequence with this word
                # We can add this word to the sequence
                # The new last character is the original last character of the word
                new_last_char = word[-1]
                new_reversed_words = reversed_words + (False,)
                result = dfs(word, new_last_char, new_reversed_words, reversed_count)
                if result is not None:
                    memo[state] = (reversed_count, reversed_words)
                    return (reversed_count, reversed_words)
            
            # Option 2: reverse the word
            reversed_word = word[::-1]
            if reversed_word.startswith(last_char):
                # Try to build the sequence with this reversed word
                # The new last character is the last character of the reversed word
                new_last_char = reversed_word[-1]
                new_reversed_words = reversed_words + (True,)
                result = dfs(reversed_word, new_last_char, new_reversed_words, reversed_count + 1)
                if result is not None:
                    memo[state] = (reversed_count + 1, new_reversed_words)
                    return (reversed_count + 1, new_reversed_words)
            
            # If neither option works, return None
            memo[state] = None
            return None
        
        # Try to build a valid sequence starting with each word
        min_reversals = float('inf')
        best_reversed_words = []
        
        for i, word in enumerate(words):
            # Try to build a sequence starting with this word
            # We can choose to reverse it or not
            # If we don't reverse it, the last character is the original last character
            # If we do reverse it, the last character is the reversed last character
            
            # Try both options
            # Option 1: do not reverse the word
            result = dfs(word, word[-1], (False,), 0)
            if result is not None:
                reversed_count, reversed_words = result
                if reversed_count < min_reversals:
                    min_reversals = reversed_count
                    best_reversed_words = [i+1 for i in range(len(reversed_words)) if reversed_words[i]]
            
            # Option 2: reverse the word
            reversed_word = word[::-1]
            result = dfs(reversed_word, reversed_word[-1], (True,), 1)
            if result is not None:
                reversed_count, reversed_words = result
                if reversed_count < min_reversals:
                    min_reversals = reversed_count
                    best_reversed_words = [i+1 for i in range(len(reversed_words)) if reversed_words[i]]
        
        if min_reversals != float('inf'):
            results.append(str(min_reversals))
            results.append(' '.join(map(str, best_reversed_words)))
        else:
            results.append('-1')
    
    print('\n'.join(results))