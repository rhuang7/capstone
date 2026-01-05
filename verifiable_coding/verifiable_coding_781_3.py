import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    X = list(map(int, data[2:2+N]))
    
    # Compute prefix XOR
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i+1] = prefix_xor[i] ^ X[i]
    
    # For each position i, the XOR of subarray X[i...i+K-1] is prefix_xor[i+K] ^ prefix_xor[i]
    # We need this XOR to be 1
    # So, prefix_xor[i+K] ^ prefix_xor[i] == 1
    # Which implies prefix_xor[i+K] != prefix_xor[i]
    
    min_flips = float('inf')
    
    # We can use a sliding window approach
    # We need to find the number of positions i where prefix_xor[i] != prefix_xor[i+K]
    # For each such position, we need to flip the bits in the subarray X[i...i+K-1] to make the XOR 1
    # The number of flips is the number of 1s in the subarray (since we need to flip them to 0 or vice versa)
    
    # Precompute the number of 1s in each window of size K
    # Using a sliding window approach
    window_ones = [0] * (N - K + 1)
    for i in range(N - K + 1):
        window_ones[i] = sum(X[i:i+K])
    
    # Now, for each window, if prefix_xor[i] != prefix_xor[i+K], we need to flip the window
    # The number of flips is the number of 1s in the window
    for i in range(N - K + 1):
        if prefix_xor[i] != prefix_xor[i+K]:
            min_flips = min(min_flips, window_ones[i])
    
    print(min_flips)

if __name__ == '__main__':
    solve()