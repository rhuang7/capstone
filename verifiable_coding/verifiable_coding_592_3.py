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
        
        # Preprocess the dictionary to allow efficient lookups
        # We'll use a trie for efficient substring checking
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
        # The grundy number for a position i is the mex of all grundy numbers
        # of positions reachable from i by removing a valid substring
        
        n = len(S)
        grundy = [0] * (n + 1)  # grundy[i] is the grundy number for the substring S[0:i]
        
        for i in range(1, n + 1):
            # Compute grundy[i] as mex of all grundy[j] where j < i and S[j:i] is in the dictionary
            reachable = set()
            for j in range(i):
                substr = S[j:i]
                if substr in dictionary:
                    reachable.add(grundy[j])
            grundy[i] = 0
            for g in range(len(reachable) + 1):
                if g not in reachable:
                    grundy[i] = g
                    break
        
        if grundy[n] == 0:
            print("Tracy")
        else:
            print("Teddy")

if __name__ == '__main__':
    solve()