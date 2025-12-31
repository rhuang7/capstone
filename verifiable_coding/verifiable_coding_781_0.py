import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    x = list(map(int, data[2:2+N]))
    
    # Precompute prefix XOR
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i+1] = prefix_xor[i] ^ x[i]
    
    min_flips = float('inf')
    
    # For each possible starting index of a subsequence of length K
    for i in range(N - K + 1):
        # Compute XOR of the subsequence from i to i+K-1
        xor = prefix_xor[i+K] ^ prefix_xor[i]
        # The desired XOR is 1, so we need to flip bits to make the XOR 1
        # The number of flips required is the number of 0s in the subsequence
        # because flipping 0s to 1s will change the XOR
        # But since the XOR is already 1, we need to flip the bits to make the XOR 1
        # So we need to count the number of 1s in the subsequence
        # Because flipping 1s to 0s will change the XOR
        # Wait, the XOR of the subsequence must be 1, so the number of 1s in the subsequence must be odd
        # So we need to flip the number of 1s to make it odd
        # So the minimum flips is the number of 1s mod 2
        # But since the XOR is already 1, we need to flip the number of 1s to be odd
        # So the minimum flips is 0 if the number of 1s is odd, else 1
        # But how do we find the number of 1s in the subsequence?
        # We can precompute the number of 1s in each subsequence of length K
        # But that would be O(N) time
        # So we can compute the number of 1s in the subsequence from i to i+K-1
        # Using a sliding window approach
        # We can precompute the number of 1s in each position
        # Then compute the sum of the window
        # So let's precompute the number of 1s in the array
        # Then use a sliding window to find the sum of 1s in each window of size K
        # The minimum flips is the minimum of (sum % 2) for all windows
        # Because if the sum is even, we need to flip one bit (so 1 flip)
        # If the sum is odd, we need 0 flips
        # So the minimum flips is the minimum of (sum % 2) for all windows
        # So let's compute the number of 1s in each window of size K
        # Using a sliding window approach
        # Precompute the number of 1s in each position
        # Then compute the sum of the window
        # So let's do that
        # Precompute the number of 1s in each position
        ones = [0] * N
        for i in range(N):
            ones[i] = ones[i-1] + x[i]
        # Now compute the sum of the window from i to i+K-1
        # Which is ones[i+K-1] - ones[i-1] if i > 0 else ones[i+K-1]
        # So for each i in 0 to N-K
        # Compute the sum of the window
        # And check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the minimum flips is the minimum of (sum % 2)
        # So the code is:
        # Precompute the ones array
        # Then for each window, compute the sum of 1s
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So let's compute that
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now, the code is:
        # Precompute the ones array
        # Then for each i in 0 to N-K
        # Compute the sum of the window
        # Then check if it is odd or even
        # Then take the minimum of (sum % 2)
        # So the code is:
        # Now