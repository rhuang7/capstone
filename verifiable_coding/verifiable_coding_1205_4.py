import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    S_list = data[1:T+1]

    total = 0

    for S in S_list:
        n = len(S)
        total += n * (n - 1) // 2  # Initial count of adjacent pairs in original string

        # For each position i, count how many times it is flipped and how it affects adjacent pairs
        # We need to consider the effect of flipping S[i] on the adjacent pairs (i-1, i) and (i, i+1)
        # For each i, we calculate how many intervals [L, R] include i and flip it, and how that affects the adjacent pairs

        # We'll use a prefix sum approach to count how many times each position is flipped
        # and then compute the contribution to the total

        # Initialize arrays for the number of flips at each position and the contribution to adjacent pairs
        flip_count = [0] * (n + 2)  # 1-based indexing
        contrib = [0] * (n + 2)  # 1-based indexing

        for i in range(1, n + 1):
            # For each position i, the number of intervals [L, R] that include i is i*(n - i + 1)
            # So we add this to flip_count[i]
            flip_count[i] = i * (n - i + 1)

        # Now, we compute the contribution of each flip to adjacent pairs
        for i in range(1, n + 1):
            # The flip at position i affects the pairs (i-1, i) and (i, i+1)
            # So we add the contribution of flip_count[i] to these pairs
            contrib[i-1] += flip_count[i]
            contrib[i] += flip_count[i]

        # Now, we compute the total contribution from all intervals
        # The initial total is n*(n-1)//2, and we add the contribution from all flips
        # Each flip contributes to the number of adjacent pairs that are equal
        # So the total is initial_total + sum(contrib[i] for i in 1..n-1)

        # But we need to subtract the original contribution from the original string
        # Because the original contribution is already counted in the initial_total
        # So we need to compute the difference between the flipped and original contributions

        # The original contribution is the number of adjacent pairs that are equal in the original string
        original_contrib = 0
        for i in range(n - 1):
            if S[i] == S[i + 1]:
                original_contrib += 1

        # Now, the total is initial_total + sum(contrib[i] for i in 1..n-1) - original_contrib
        # Because the initial_total already includes the original_contrib
        # So we need to subtract it once

        total += sum(contrib[1:n]) - original_contrib

    print(total)

if __name__ == '__main__':
    solve()