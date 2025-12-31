import sys
from collections import deque

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
        dict_words = []
        for _ in range(N):
            dict_words.append(data[idx])
            idx += 1
        
        # Preprocess dictionary words
        dict_set = set(dict_words)
        
        # Precompute all possible substrings of S
        substrings = set()
        for i in range(len(S)):
            for j in range(i + 1, len(S) + 1):
                substrings.add(S[i:j])
        
        # Precompute all possible substrings in the dictionary
        dict_substrings = set(dict_words)
        
        # Find all substrings of S that are in the dictionary
        valid_moves = [s for s in substrings if s in dict_substrings]
        
        # If no valid moves, Tracy wins
        if not valid_moves:
            print("Tracy")
            continue
        
        # Use dynamic programming to determine winning positions
        # dp[i] = True if the current player can win starting from position i
        dp = [False] * (len(S) + 1)
        
        # Fill dp from the end
        for i in range(len(S) - 1, -1, -1):
            for j in range(i + 1, len(S) + 1):
                substr = S[i:j]
                if substr in dict_substrings:
                    # Check if any move leads to a losing position for the opponent
                    for k in range(j, len(S) + 1):
                        if not dp[k]:
                            dp[i] = True
                            break
                    # If any move leads to a losing position, current player can win
                    if dp[i]:
                        break
        
        # If dp[0] is True, Teddy wins, else Tracy wins
        if dp[0]:
            print("Teddy")
        else:
            print("Tracy")

if __name__ == '__main__':
    solve()