def check(candidate):
    assert candidate([1, 20, 6, 4, 5], 5) == 5
    assert candidate([8, 4, 2, 1], 4) == 6
    assert candidate([3, 1, 2], 3) == 2


def count_inversions(arr):
    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_inversions = merge_sort_and_count(arr[:mid])
        right, right_inversions = merge_sort_and_count(arr[mid:])
        merged, merge_inversions = merge(left, right)
        total_inversions = left_inversions + right_inversions + merge_inversions
        return merged, total_inversions

    def merge(left, right):
        result = []
        i = j = 0
        inversions = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inversions += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions

    _, total = merge_sort_and_count(arr)
    return total

check(count_inversions)