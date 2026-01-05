import sys
from functools import lru_cache

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        S = data[idx]
        idx += 1
        N = int(data[idx])
        idx += 1
        dictionary = []
        for _ in range(N):
            dictionary.append(data[idx])
            idx += 1
        
        # Preprocess dictionary for faster lookups
        dict_set = set(dictionary)
        
        # Precompute all possible substrings of S
        substrings = set()
        for i in range(len(S)):
            for j in range(i + 1, len(S) + 1):
                substrings.add(S[i:j])
        
        # Check if a substring is in the dictionary
        def is_in_dict(s):
            return s in dict_set
        
        # Memoization for game states
        @lru_cache(maxsize=None)
        def can_win(start, end):
            # If no move is possible, current player loses
            if start >= end:
                return False
            # Try all possible substrings in the current range
            for i in range(start, end):
                for j in range(i + 1, end + 1):
                    substr = S[start:j]
                    if is_in_dict(substr):
                        # If the current player can take this substring and the next player loses
                        if not can_win(start, i) and not can_win(j, end):
                            return True
            return False
        
        # Determine the winner
        if can_win(0, len(S) - 1):
            results.append("Teddy")
        else:
            results.append("Tracy")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()