import sys
import bisect

def count_inversions(arr):
    sorted_arr = sorted(arr)
    inv_count = 0
    for i in range(len(arr)):
        inv_count += bisect.bisect_left(sorted_arr, arr[i])
        bisect.insort(sorted_arr, arr[i])
    return inv_count

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
        inv_in_A = count_inversions(A)
        inv_between = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inv_between += K * (K - 1) // 2
        inv_within = inv_in_A * K * (K - 1) // 2
        total_inv = inv_between + inv_within
        results.append(total_inv)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()