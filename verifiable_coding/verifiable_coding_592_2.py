import sys
from collections import defaultdict

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
        dict_words = set()
        for _ in range(N):
            dict_words.add(data[idx])
            idx += 1
        
        # Preprocess the dictionary words to a trie
        class TrieNode:
            def __init__(self):
                self.children = {}
        
        root = TrieNode()
        for word in dict_words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
        
        # Function to check if a substring is in the dictionary
        def is_in_dict(s, start, end):
            node = root
            for i in range(start, end + 1):
                ch = s[i]
                if ch not in node.children:
                    return False
                node = node.children[ch]
            return True
        
        # Game simulation using Grundy numbers
        # dp[i] is the Grundy number for the substring S[i:]
        dp = [0] * (len(S) + 1)
        
        for i in range(len(S) - 1, -1, -1):
            # Check all possible substrings starting at i
            for j in range(i, len(S)):
                # Check if S[i:j+1] is in the dictionary
                if is_in_dict(S, i, j):
                    # Find the mex of all dp[k] where k is the next position after removing this substring
                    mex = 0
                    seen = set()
                    for k in range(i + 1, len(S) + 1):
                        if k > j + 1:
                            break
                        seen.add(dp[k])
                    while mex in seen:
                        mex += 1
                    dp[i] = mex
        
        if dp[0] == 0:
            print("Tracy")
        else:
            print("Teddy")

if __name__ == '__main__':
    solve()