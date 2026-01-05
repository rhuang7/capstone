import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0]
    T = data[1]
    Q = int(data[2])
    queries = list(map(int, data[3:3+Q]))
    
    len_S = len(S)
    len_T = len(T)
    
    # Precompute the positions of T in S
    # We need to find all starting positions in S where T occurs
    # and then for each row, determine how many times T appears
    # based on the positions and the row number
    
    # Precompute all starting positions in S where T occurs
    # We can use the Knuth-Morris-Pratt (KMP) algorithm for this
    # But for the sake of time, we'll use a simple approach for now
    # and assume that T is not too long
    
    # Precompute the occurrences of T in S
    occurrences = []
    for i in range(len_S - len_T + 1):
        if S[i:i+len_T] == T:
            occurrences.append(i)
    
    # Precompute the positions where T starts in the row
    # For a row N, the row has N characters
    # The row starts with S[0], then S[1], then S[2], etc.
    # The characters are repeated in a cyclic manner
    
    # For a given row N, the characters are:
    # S[0], S[1], S[2], ..., S[N-1], S[0], S[1], ..., S[N-1], ...
    # So the total number of characters is N, and the pattern repeats every len(S)
    
    # For a given row N, the number of full cycles is N // len(S)
    # The remaining characters are N % len(S)
    
    # For each occurrence of T in S, we can determine how many times it appears in the row
    # The occurrence starts at position i in S
    # The row has N characters, so the occurrence can start at position i + k * len(S)
    # where k is an integer such that the occurrence is within the row
    
    # For each occurrence of T in S, we can compute how many times it appears in the row
    
    # For a given row N, the number of times T appears is the number of valid starting positions
    # where T can be found in the row
    
    # We precompute for each occurrence of T in S, the positions where it can appear in the row
    
    # For each occurrence of T in S, we compute the number of times it appears in the row
    # For a row N, the number of times T appears is the number of valid starting positions
    # where T can be found in the row
    
    # For each occurrence of T in S, the starting position in the row can be:
    # i + k * len(S), where k is such that i + k * len(S) + len_T - 1 < N
    
    # So for each occurrence of T in S, the number of valid k's is floor((N - i - len_T + 1) / len(S)) + 1
    
    # So for each occurrence of T in S, the number of times it appears in the row is:
    # floor((N - i - len_T + 1) / len(S)) + 1 if i + len_T <= N
    # else 0
    
    # So for each query N, we can compute the answer as the sum over all occurrences of T in S of the number of times they appear in the row
    
    # Now, for each query N, we compute the answer
    
    for N in queries:
        ans = 0
        for i in occurrences:
            if i + len_T > N:
                continue
            # Compute how many times this occurrence appears in the row
            # The starting positions are i + k * len(S), where k >= 0
            # and i + k * len(S) + len_T - 1 < N
            # So k can be from 0 to floor((N - i - len_T) / len(S))
            # So the number of such k is floor((N - i - len_T) / len(S)) + 1
            # But we need to make sure that i + k * len(S) + len_T - 1 < N
            # So the maximum k is floor((N - i - len_T) / len(S))
            # So the number of k is floor((N - i - len_T) / len(S)) + 1
            # But we also need to check if i + len_T <= N
            # So the number of times this occurrence appears is:
            # max(0, floor((N - i - len_T) / len(S)) + 1)
            # But we also need to make sure that i + k * len(S) + len_T - 1 < N
            # So the maximum k is floor((N - i - len_T) / len(S))
            # So the number of k is floor((N - i - len_T) / len(S)) + 1
            # But we need to check if i + len_T <= N
            # So if i + len_T > N, then this occurrence cannot appear in the row
            # So we skip it
            # So for i + len_T <= N
            # compute the number of times this occurrence appears in the row
            # which is floor((N - i - len_T) / len(S)) + 1
            # But we also need to make sure that i + k * len(S) + len_T - 1 < N
            # which is already handled by the calculation
            # So the number of times this occurrence appears is:
            # max(0, floor((N - i - len_T) / len(S)) + 1)
            # But we need to check if i + len_T <= N
            # So the number of times this occurrence appears is:
            # if i + len_T > N:
            #     0
            # else:
            #     floor((N - i - len_T) / len(S)) + 1
            # So we can compute it as:
            # if i + len_T > N:
            #     continue
            # else:
            #     k_max = (N - i - len_T) // len(S)
            #     ans += k_max + 1
            # So we compute this
            if i + len_T <= N:
                k_max = (N - i - len_T) // len(S)
                ans += k_max + 1
        print(ans)

if __name__ == '__main__':
    solve()