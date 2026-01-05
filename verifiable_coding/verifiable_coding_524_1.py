import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0].decode()
    Q = int(data[1])
    queries = [(int(data[2 + 2*i]), int(data[2 + 2*i + 1])) for i in range(Q)]
    
    # Preprocess: count frequency of each character
    freq = [0] * 26
    for c in S:
        idx = ord(c) - ord('a')
        freq[idx] += 1
    
    # Preprocess: for each position, store the character's value
    char_values = [ord(c) - ord('a') + 1 for c in S]
    
    # Preprocess: for each position, store whether the value is even and unique
    # We'll create a prefix sum array for even unique values
    prefix = [0] * (len(S) + 1)
    for i in range(len(S)):
        val = char_values[i]
        if val % 2 == 0:
            # Check if this value has been seen before
            if freq[val - 1] == 1:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        else:
            prefix[i + 1] = prefix[i]
    
    # Process queries
    for x, y in queries:
        # Convert x and y to 1-based indices
        res = prefix[y] - prefix[x - 1]
        print(res)
        
if __name__ == '__main__':
    solve()