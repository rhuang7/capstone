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
        # This is equivalent to finding the longest increasing subsequence in b_i
        # where a_i is non-decreasing
        # So we can use a greedy algorithm with binary search
        # To find the longest increasing subsequence in b_i
        # We will maintain a list 'tails' where tails[i] is the smallest possible
        # last element of an increasing subsequence of length i+1
        tails = []
        for a, b in shares:
            # Find the first element in tails >= b
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