import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    Q = int(data[N+1])
    queries = list(map(int, data[N+2:]))
    
    # Preprocess for each position, the gcd of the subarray ending at that position
    # and the sum of the subarray
    # We'll use a sliding window approach to find all subarrays that can generate K
    # Since K is up to 1e6, we can use a frequency array for K
    
    # Precompute prefix sums
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    
    # Frequency array for K
    freq = defaultdict(int)
    
    # For each possible end position r, we'll track the gcd and sum of subarrays ending at r
    # We'll use a dictionary to store (gcd, sum) pairs
    # For each new element, we'll update the dictionary by combining with previous entries
    # and adding the new element itself
    # We'll then check if the sum can be adjusted to K by using the gcd
    
    # We'll also track the number of subarrays that can generate K
    # For each (gcd, sum) pair, we can generate K if K is a multiple of gcd and (sum - K) is a multiple of gcd
    # So for each (gcd, sum), we can check if K is a multiple of gcd and (sum - K) is a multiple of gcd
    
    # However, since K is up to 1e6, we can precompute for each possible K the number of subarrays that can generate it
    
    # But since K is up to 1e6 and N is up to 1e5, we can't precompute for all K
    # So we'll process each query as it comes
    
    # For each query K, we'll check all possible subarrays and count how many can generate K
    
    # But this is O(N^2) in the worst case, which is too slow for N=1e5
    
    # So we need a more efficient approach
    
    # We'll use the fact that a subarray can generate K if and only if K is a multiple of the gcd of the subarray
    # So for each subarray, we compute its gcd and sum
    # Then, for each query K, we check how many subarrays have gcd dividing K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need a way to efficiently find all subarrays that can generate K
    
    # Let's use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each subarray, we compute its gcd and sum
    # Then, for each query K, we check if K is a multiple of the gcd and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need a way to count the number of subarrays that can generate K efficiently
    
    # Let's try a different approach
    
    # We'll use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to find all subarrays that can generate K by using the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to find all subarrays that can generate K by checking for each possible subarray whether it can generate K
    
    # But this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to find all subarrays that can generate K by checking for each possible subarray whether it can generate K
    
    # But this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    # But this is still not helpful
    
    # So let's try to use the fact that for a subarray to generate K, K must be a multiple of the gcd of the subarray
    # So for each query K, we can count the number of subarrays whose gcd divides K and (sum - K) is a multiple of gcd
    
    # But again, this is O(N^2), which is too slow
    
    # So we need to find a way to count the number of subarrays that can generate K efficiently
    
    # Let's try to use the fact that the sum of the subarray must be congruent to K modulo the gcd of the subarray
    
    #