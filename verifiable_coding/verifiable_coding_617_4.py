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
        shares = []
        for _ in range(N):
            a = int(data[idx])
            b = int(data[idx + 1])
            idx += 2
            shares.append((a, b))
        # Sort shares by a_i in ascending order and by b_i in descending order
        shares.sort(key=lambda x: (x[0], -x[1]))
        # Find the longest increasing subsequence of b_i
        # Since a_i is already sorted, we only need to check b_i
        # We can use a greedy approach with binary search
        # to find the length of the longest increasing subsequence
        # of b_i
        # This is O(N log N) time
        # Initialize a list to store the smallest possible tail of all increasing subsequences
        # with length i+1
        tails = []
        for a, b in shares:
            # Use binary search to find the first element in tails greater than or equal to b
            # and replace it with b
            # This maintains the smallest possible tail for each length
            # We use the bisect module for this
            import bisect
            idx_b = bisect.bisect_left(tails, b)
            if idx_b == len(tails):
                tails.append(b)
            else:
                tails[idx_b] = b
        results.append(len(tails))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()