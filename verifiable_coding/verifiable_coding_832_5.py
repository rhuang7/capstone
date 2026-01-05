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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        A.sort()
        # Find the minimum sum subsequence of size K
        min_sum = sum(A[:K])
        # Count how many times the smallest K elements appear
        count = 0
        # Find the number of elements equal to A[K-1]
        target = A[K-1]
        # Count how many elements are equal to target in the first K elements
        cnt = 0
        for i in range(K):
            if A[i] == target:
                cnt += 1
        # Now count how many elements in the entire array are equal to target
        total_cnt = 0
        for num in A:
            if num == target:
                total_cnt += 1
        # The number of interesting subsequences is combination(total_cnt, cnt)
        from math import comb
        results.append(comb(total_cnt, cnt))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()