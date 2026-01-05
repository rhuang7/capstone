import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    x = list(map(int, data[2:2+N]))
    
    # Compute prefix xor
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i+1] = prefix_xor[i] ^ x[i]
    
    # For each position i, the xor of subarray x[i...i+K-1] is prefix_xor[i+K] ^ prefix_xor[i]
    # We want this to be 1
    # So prefix_xor[i+K] ^ prefix_xor[i] == 1
    # Which means prefix_xor[i+K] != prefix_xor[i]
    
    min_flips = float('inf')
    
    for i in range(N - K + 1):
        if prefix_xor[i + K] != prefix_xor[i]:
            # The subarray x[i...i+K-1] is already valid, no flips needed
            min_flips = 0
            break
    
    # If no valid subarray found, we need to flip exactly K bits to make one subarray valid
    # So the minimum flips is K
    print(min_flips if min_flips != float('inf') else K)

if __name__ == '__main__':
    solve()