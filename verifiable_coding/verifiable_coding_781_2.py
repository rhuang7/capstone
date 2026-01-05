import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    X = list(map(int, data[2:2+N]))
    
    # Precompute prefix XOR
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i+1] = prefix_xor[i] ^ X[i]
    
    min_flips = float('inf')
    
    # For each possible starting index of a subarray of length K
    for i in range(N - K + 1):
        # Compute XOR of subarray X[i...i+K-1]
        xor = prefix_xor[i+K] ^ prefix_xor[i]
        # The desired XOR is 1, so we need to flip bits to make the XOR 1
        # The number of flips is the number of bits that differ from the desired XOR
        # Since XOR is 1, we need to flip the bits in the subarray such that their XOR is 1
        # This is equivalent to flipping the bits in the subarray such that the XOR is 1
        # We can compute the number of 1s in the subarray and compare to K
        # If the number of 1s is even, we need to flip one bit (so that XOR becomes 1)
        # If the number of 1s is odd, we need to flip zero bits (so that XOR is 1)
        # So the number of flips is (number of 1s % 2)
        # But how to compute the number of 1s in the subarray?
        # We can use a sliding window approach to count the number of 1s
        # But since we already have the prefix_xor, we can use it to find the number of 1s
        # However, we need to find the number of 1s in the subarray X[i...i+K-1]
        # We can compute it as the sum of X[i...i+K-1]
        # But since X is a list of 0s and 1s, we can compute the sum
        # However, for large N, we need an efficient way to compute the sum of any subarray
        # So we can precompute a prefix sum array
        # Let's precompute prefix_sum
        # But since we already have prefix_xor, we can use it to find the number of 1s
        # The XOR of the subarray is 1, so the number of 1s in the subarray must be odd
        # So the number of flips is 0 if the number of 1s is odd, else 1
        # But how to compute the number of 1s in the subarray?
        # We can compute the sum of the subarray
        # So we need to precompute prefix_sum
        # Let's precompute prefix_sum
        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i+1] = prefix_sum[i] + X[i]
        
        sum_sub = prefix_sum[i+K] - prefix_sum[i]
        flips = sum_sub % 2
        min_flips = min(min_flips, flips)
    
    print(min_flips)

if __name__ == '__main__':
    solve()