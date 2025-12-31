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
        # We can use a greedy algorithm with binary search
        # This is similar to the Longest Increasing Subsequence problem
        # But since we want the maximum number of shares, we can use a patience sorting approach
        # We'll use a list to keep track of the smallest possible tail of all increasing subsequences
        # with length i+1
        tails = []
        for a, b in shares:
            # Find the first element in tails that is >= b
            # Using binary search
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= b:
                    right = mid
                else:
                    left = mid + 1
            if left == len(tails):
                tails.append(b)
            else:
                tails[left] = b
        results.append(len(tails))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()