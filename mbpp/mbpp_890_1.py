def check(candidate):
    assert candidate([1,2,3,4],[1,2,3],3) == 3
    assert candidate([2,4,6,8,10],[2,4,6,8],4) == 4
    assert candidate([1,3,5,7,9,11],[1,3,5,7,9],5) == 5


def find_extra_element_index(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    
    # If arr1 has one more element than arr2, arr1 has the extra element
    if n == m + 1:
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            # Compare elements at mid and mid+1 in arr1
            if arr1[mid] == arr1[mid + 1]:
                # The extra element is in the right half
                left = mid + 1
            else:
                # The extra element is in the left half or at mid
                right = mid - 1
        return left
    # If arr2 has one more element than arr1, arr2 has the extra element
    elif m == n + 1:
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            # Compare elements at mid and mid+1 in arr2
            if arr2[mid] == arr2[mid + 1]:
                # The extra element is in the right half
                left = mid + 1
            else:
                # The extra element is in the left half or at mid
                right = mid - 1
        return left
    # If arrays are of equal length, no extra element
    else:
        return -1

check(find_extra_element_index)