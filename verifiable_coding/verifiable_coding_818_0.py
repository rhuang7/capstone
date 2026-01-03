import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        for __ in range(Q):
            L = int(data[idx]) - 1
            R = int(data[idx+1]) - 1
            idx += 2
            # Bitwise AND of A[L...R] is even or odd?
            # The bitwise AND is odd if and only if all numbers in the range have the least significant bit (LSB) as 1.
            # So check if there is at least one even number in the range.
            # If there is at least one even number, the AND will be even.
            # Otherwise, it will be odd.
            # So we need to check if there is any even number in A[L...R]
            # To do this efficiently, precompute prefix sums of even counts
            # But since the range can be up to 1e5 and Q is up to 1e5, we need O(1) per query
            # So we can precompute a prefix array of even counts
            # But since we can't precompute for all test cases, we'll check on the fly
            # However, for large N and Q, this will be O(Q*N) which is too slow
            # So we need a better way
            # The key insight is: the bitwise AND of a range is even if and only if there is at least one even number in the range
            # Because if there is at least one even number, the AND will be even
            # If all numbers are odd, the AND will be odd
            # So for each query, check if there is at least one even number in A[L...R]
            # To do this efficiently, we can precompute a prefix array of even counts
            # So we precompute prefix_even[i] = number of even numbers in A[0...i-1]
            # Then for query [L, R], the count is prefix_even[R+1] - prefix_even[L]
            # If this count > 0, then the AND is even, else it's odd
            # So let's precompute prefix_even
            prefix_even = [0] * (N + 1)
            for i in range(N):
                prefix_even[i+1] = prefix_even[i] + (1 if A[i] % 2 == 0 else 0)
            even_count = prefix_even[R+1] - prefix_even[L]
            if even_count > 0:
                results.append("EVEN")
            else:
                results.append("ODD")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()