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
        def merge_sort_count(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, left_count = merge_sort_count(arr[:mid])
            right, right_count = merge_sort_count(arr[mid:])
            merged, merge_count = merge(left, right)
            
            total_count = left_count + right_count + merge_count
            return merged, total_count
        
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
                    j += 1
                    count += len(left) - i
            
            merged += left[i:]
            merged += right[j:]
            return merged, count
        
        _, total_inversions = merge_sort_count(arr)
        results.append(str(total_inversions))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()