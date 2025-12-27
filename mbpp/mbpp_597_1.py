def check(candidate):
    assert candidate([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5) == 6
    assert candidate([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7) == 256
    assert candidate([3, 4, 7, 8, 10], [2, 5, 9, 11], 5, 4, 6) == 8


def find_kth_element(arr1, arr2, k):
    # Handle edge cases
    if not arr1:
        return arr2[k-1]
    if not arr2:
        return arr1[k-1]
    
    # Ensure arr1 is the smaller array for efficiency
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    
    # Binary search approach to find the kth element
    left, right = 0, len(arr1)
    
    while left <= right:
        mid = (left + right) // 2
        mid2 = k - mid
        
        # Check if mid is the correct partition
        if mid2 < 0:
            right = mid - 1
        elif mid2 > len(arr2):
            left = mid + 1
        else:
            # Compare elements at the partition
            a1 = arr1[mid-1] if mid > 0 else float('-inf')
            a2 = arr2[mid2-1] if mid2 > 0 else float('-inf')
            b1 = arr1[mid] if mid < len(arr1) else float('inf')
            b2 = arr2[mid2] if mid2 < len(arr2) else float('inf')
            
            if a1 > b2 or a2 > b1:
                if a1 > b2:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return max(a1, a2) if k == mid + mid2 else min(b1, b2)

check(find_kth_element)