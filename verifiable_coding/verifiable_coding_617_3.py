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
        # Find the maximum number of shares that can be sold
        # We need to select shares such that a_i <= a_j and b_i < b_j
        # This is equivalent to selecting a chain of shares where each subsequent share has a higher a_i and higher b_i
        # So we can use a greedy approach: sort by a_i and then by b_i in descending order, then count the longest increasing subsequence in b_i
        b_values = [b for a, b in shares]
        # Longest increasing subsequence (LIS) of b_values
        # Since a_i is sorted, we only need to consider b_i
        # Use a O(N log N) algorithm for LIS
        lis = []
        for b in b_values:
            # Use bisect to find the first element in lis >= b
            # Replace it with b to maintain the longest increasing subsequence
            idx_b = bisect.bisect_left(lis, b)
            if idx_b == len(lis):
                lis.append(b)
            else:
                lis[idx_b] = b
        results.append(len(lis))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()