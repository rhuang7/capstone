def check(candidate):
    assert candidate([1,0,2],3) == True
    assert candidate([1,2,0],3) == False
    assert candidate([1,2,1],3) == True


def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
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

    _, total_inv = merge_sort(arr)
    return total_inv

def have_same_inversion_count(arr1, arr2):
    return count_inversions(arr1) == count_inversions(arr2)

check(have_same_inversion_count)