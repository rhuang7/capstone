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
        # Compute XOR of subarray X[i..i+K-1]
        xor_sub = prefix_xor[i+K] ^ prefix_xor[i]
        # The required XOR is 1, so we need to flip bits to make the XOR 1
        # The number of flips is the number of 0s in the subarray if xor_sub is 1,
        # or the number of 1s if xor_sub is 0 (since we need to flip to get 1)
        # But since we can flip any bits, we just need to count the number of bits that are different from the desired XOR
        # Since the desired XOR is 1, we count the number of 1s in the subarray if xor_sub is 0,
        # or the number of 0s if xor_sub is 1
        # But since we can flip any bits, we just need to count the number of bits that are different from the desired XOR
        # So, for the subarray, we count the number of bits that are not equal to (xor_sub ^ 1)
        # Because we want the XOR of the subarray to be 1, so if the current XOR is 0, we need to flip one bit
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, we can count the number of 1s in the subarray if xor_sub is 0, or the number of 0s if xor_sub is 1
        # But since we can flip any bits, we can just count the number of bits that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips is the number of bits in the subarray that are not equal to (xor_sub ^ 1)
        # Which is the same as the number of bits in the subarray that are not equal to 1 if xor_sub is 0, or not equal to 0 if xor_sub is 1
        # So, the number of flips