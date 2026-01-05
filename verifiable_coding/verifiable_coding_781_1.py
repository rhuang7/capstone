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
    # We need this to be 1, so prefix_xor[i+K] ^ prefix_xor[i] == 1
    # Which means prefix_xor[i+K] != prefix_xor[i]
    
    min_flips = float('inf')
    
    for i in range(N - K + 1):
        if prefix_xor[i + K] != prefix_xor[i]:
            # The subarray from i to i+K-1 is already valid, so no flips needed
            min_flips = 0
            break
    
    # If no valid subarray found, we need to flip exactly one bit in the array
    # So the minimum flips is 1
    print(min_flips if min_flips != float('inf') else 1)

if __name__ == '__main__':
    solve()