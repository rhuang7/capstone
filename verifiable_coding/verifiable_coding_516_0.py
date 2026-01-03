import sys
import bisect

def count_inversions(arr):
    temp = [0] * len(arr)
    return merge_sort(arr, temp, 0, len(arr) - 1)

def merge_sort(arr, temp, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    inv_count = merge_sort(arr, temp, left, mid)
    inv_count += merge_sort(arr, temp, mid + 1, right)
    inv_count += merge(arr, temp, left, mid, right)
    return inv_count

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]
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
        original_inversions = count_inversions(A)
        total_inversions = original_inversions * K * (K - 1) // 2
        # Calculate inversions between different copies
        for i in range(N):
            for j in range(i + 1, N):
                if A[i] > A[j]:
                    total_inversions += K * (K - 1)
        results.append(str(total_inversions))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()