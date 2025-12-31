import sys

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
        s = data[idx]
        idx += 1
        
        # We need to assign each character to a subsequence such that no two adjacent characters are the same
        # We can track the last used pattern for each subsequence
        # For each character, we try to assign it to the first subsequence that has the opposite last character
        # If none, we start a new subsequence
        
        # We'll keep track of the last character of each subsequence
        # And the current number of subsequences
        last_chars = []
        k = 0
        
        for c in s:
            found = False
            for i in range(len(last_chars)):
                if last_chars[i] != c:
                    last_chars[i] = c
                    found = True
                    break
            if not found:
                last_chars.append(c)
                k += 1
        
        # Now we need to assign the indices to the subsequences
        # We'll track for each subsequence the last character and the positions
        # We'll use a list of lists to store the positions for each subsequence
        # And then assign the indices accordingly
        subseq_positions = [[] for _ in range(k)]
        for i, c in enumerate(s):
            for j in range(k):
                if subseq_positions[j] and subseq_positions[j][-1] != c:
                    subseq_positions[j].append(i)
                    break
            else:
                subseq_positions[k-1].append(i)
        
        # Now create the output list
        output = [1] * n
        for i in range(k):
            for pos in subseq_positions[i]:
                output[pos] = i + 1
        
        results.append(f"{k}")
        results.append(" ".join(map(str, output)))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()