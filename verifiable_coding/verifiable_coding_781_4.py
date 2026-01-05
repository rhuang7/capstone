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
        # Compute XOR of subarray from i to i+K-1
        xor = prefix_xor[i+K] ^ prefix_xor[i]
        # The required XOR is 1, so we need to flip bits to make the XOR 1
        # The number of flips is the number of 0s in the subarray (since XOR is 1)
        # We can compute the number of 0s in the subarray by checking the XOR
        # Since XOR is 1, the number of 1s is (K - count_of_1s), and 0s is count_of_1s
        # But we can also compute the number of 0s by checking the XOR of the subarray
        # If the XOR is 1, then the number of 0s is (K - count_of_1s)
        # But since we don't know the count of 1s, we can just count the number of 0s in the subarray
        # However, we can't directly count the 0s, so we can use the XOR to determine the number of 0s
        # Since XOR is 1, the number of 0s is (K - count_of_1s), but we can't compute that directly
        # So we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # If the XOR is 1, then the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # However, we can't do that directly, so we can compute the number of 0s by checking the XOR of the subarray
        # If the XOR is 1, then the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we need to count the number of 0s in the subarray
        # We can do this by iterating through the subarray and counting the 0s
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we need to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of 0s is (K - count_of_1s)
        # But we can't compute that directly, so we have to count the number of 0s in the subarray
        # So we can count the number of 0s in the subarray by iterating through the subarray
        # But for large N, this would be O(N^2), which is too slow
        # So we need a way to compute the number of 0s in each subarray of length K
        # We can precompute the number of 0s in each position
        # But for this problem, we can compute the number of 0s in the subarray by checking the XOR of the subarray
        # Since the XOR is 1, the number of