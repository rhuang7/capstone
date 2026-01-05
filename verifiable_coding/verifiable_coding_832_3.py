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
        # Find the minimum sum of K elements
        min_sum = sum(A[:K])
        # Count how many times the smallest K elements appear
        count = 0
        # Find the number of elements equal to A[K-1]
        target = A[K-1]
        # Count how many elements are equal to target
        cnt = 0
        for num in A:
            if num == target:
                cnt += 1
            elif num > target:
                break
        # Calculate combinations of cnt elements taken K elements at a time
        from math import comb
        results.append(comb(cnt, K))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()