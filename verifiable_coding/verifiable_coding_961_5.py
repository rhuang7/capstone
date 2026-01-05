import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        # Using a modified merge sort algorithm to count inversions
        def merge_sort_count(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, a = merge_sort_count(arr[:mid])
            right, b = merge_sort_count(arr[mid:])
            merged, c = merge(left, right)
            return merged, a + b + c
        def merge(left, right):
            merged = []
            i = j = 0
            count = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1
            merged += left[i:]
            merged += right[j:]
            return merged, count
        _, inversions = merge_sort_count(arr)
        print(inversions)

if __name__ == '__main__':
    solve()