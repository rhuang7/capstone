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
        dictionary = []
        for _ in range(N):
            dictionary.append(data[idx])
            idx += 1
        
        # Preprocess dictionary for faster lookups
        dict_set = set(dictionary)
        
        # Use dynamic programming to determine Grundy numbers
        # dp[i] represents the Grundy number for the substring S[i:]
        # We compute from the end of the string to the beginning
        n = len(S)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            # Check all possible substrings starting at i
            for j in range(i + 1, n + 1):
                substr = S[i:j]
                if substr in dict_set:
                    # Find the mex (minimum excludant) of all dp[k] where k is the next position after removing substr
                    mex = 0
                    while mex in [dp[k] for k in range(j, n + 1)]:
                        mex += 1
                    dp[i] = mex
                    break  # Only consider the first valid move for grundy number calculation
        
        # If the grundy number of the entire string is non-zero, Teddy wins; else Tracy wins
        if dp[0] != 0:
            print("Teddy")
        else:
            print("Tracy")

if __name__ == '__main__':
    solve()