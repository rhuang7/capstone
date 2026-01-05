import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    x = list(map(int, data[2:2+N]))
    
    # Compute prefix XOR
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i+1] = prefix_xor[i] ^ x[i]
    
    # For each position i, the XOR of the subarray from i to i+K-1 is prefix_xor[i+K] ^ prefix_xor[i]
    # We want this to be 1, so prefix_xor[i+K] ^ prefix_xor[i] == 1
    # Which means prefix_xor[i+K] != prefix_xor[i]
    
    min_flips = float('inf')
    
    for i in range(N - K + 1):
        if prefix_xor[i+K] != prefix_xor[i]:
            # We need to flip the bits in the subarray x[i...i+K-1] so that their XOR is 1
            # The number of flips is the number of 1s in the subarray (since we need to flip them to 0s or vice versa)
            # But since the XOR is 1, we can flip the bits to make the XOR 1
            # So the number of flips is the count of 1s in the subarray
            count = sum(x[i:i+K])
            min_flips = min(min_flips, count)
    
    print(min_flips)

if __name__ == '__main__':
    solve()