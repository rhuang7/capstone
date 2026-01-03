import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        S = data[idx]
        idx += 1
        N = int(data[idx])
        idx += 1
        dictionary = set()
        for _ in range(N):
            dictionary.add(data[idx])
            idx += 1
        
        # Preprocess the dictionary for faster lookups
        # We'll use a trie for efficient substring checks
        class TrieNode:
            def __init__(self):
                self.children = {}
        
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
        
        # Function to check if a substring exists in the dictionary
        def is_substring(s, start, end):
            node = root
            for i in range(start, end + 1):
                c = s[i]
                if c not in node.children:
                    return False
                node = node.children[c]
            return True
        
        # Game simulation using Grundy numbers (Sprague-Grundy theorem)
        # We'll compute the Grundy number for each position in the string
        # The game is a variant of the impartial game where players remove substrings
        # We'll use dynamic programming to compute the Grundy numbers
        
        n = len(S)
        grundy = [0] * (n + 1)
        
        for i in range(n):
            # Try all possible substrings starting at i
            for j in range(i, n):
                # Check if the substring S[i..j] is in the dictionary
                if is_substring(S, i, j):
                    # Compute the Grundy number for the remaining positions
                    # After removing S[i..j], the string is split into two parts
                    # So we need to compute the XOR of the Grundy numbers of the left and right parts
                    left = grundy[i]
                    right = grundy[j + 1]
                    current = grundy[i + 1] ^ right
                    if current > grundy[i]:
                        grundy[i] = current
        
        # If the grundy number of the entire string is non-zero, Teddy wins
        # Otherwise, Tracy wins
        if grundy[0] != 0:
            print("Teddy")
        else:
            print("Tracy")

if __name__ == '__main__':
    solve()