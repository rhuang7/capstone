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
        
        # Preprocess dictionary to store words in a set for quick lookup
        # Also, for each word in the dictionary, store its length
        dict_len = {word: len(word) for word in dictionary}
        
        # Use dynamic programming to determine if a substring is a winning position
        # dp[i][j] = True if the substring S[i:j] is a winning position
        n = len(S)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        
        # Base case: empty substring is a losing position
        dp[0][0] = False
        
        # Fill the dp table
        for i in range(n + 1):
            for j in range(i, n + 1):
                # Check if there's a word in the dictionary that can be removed
                for k in range(i, j + 1):
                    word = S[i:k]
                    if word in dictionary:
                        # If removing this word leads to a losing position for the opponent
                        if not dp[i][k] or not dp[k][j]:
                            dp[i][j] = True
                            break
                # If no word can be removed, it's a losing position
                if not dp[i][j]:
                    dp[i][j] = False
        
        # If the entire string is a winning position, Teddy wins; else Tracy wins
        if dp[0][n]:
            print("Teddy")
        else:
            print("Tracy")

if __name__ == '__main__':
    solve()