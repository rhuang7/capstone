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
    
    # Preprocess: for each position, determine if the character's value is even and unique
    # We'll create a prefix sum array for even unique values
    prefix = [0] * (len(S) + 1)
    for i in range(len(S)):
        c = S[i]
        idx = ord(c) - ord('a')
        if idx % 2 == 0 and freq[idx] == 1:
            prefix[i + 1] = prefix[i] + 1
        else:
            prefix[i + 1] = prefix[i]
    
    # Process queries
    for x, y in queries:
        # Convert to 0-based indices
        x -= 1
        y -= 1
        res = prefix[y + 1] - prefix[x]
        print(res)

if __name__ == '__main__':
    solve()