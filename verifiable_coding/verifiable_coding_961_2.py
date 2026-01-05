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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Using a modified merge sort algorithm to count inversions
        def merge_sort_count_inv(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, left_inv = merge_sort_count_inv(arr[:mid])
            right, right_inv = merge_sort_count_inv(arr[mid:])
            merged, merge_inv = merge(left, right)
            
            total_inv = left_inv + right_inv + merge_inv
            return merged, total_inv
        
        def merge(left, right):
            merged = []
            i = j = 0
            inv = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    inv += len(left) - i
            
            merged += left[i:]
            merged += right[j:]
            return merged, inv
        
        _, total_inv = merge_sort_count_inv(arr)
        results.append(str(total_inv))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()