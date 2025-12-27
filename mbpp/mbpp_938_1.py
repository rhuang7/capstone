def check(candidate):
    assert candidate([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)
    assert candidate([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)
    assert candidate([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)


def find_three_closest_elements(arr1, arr2, arr3):
    import bisect
    
    def get_closest(arr, target):
        index = bisect.bisect_left(arr, target)
        if index == 0:
            return arr[0]
        if index == len(arr):
            return arr[-1]
        return arr[index - 1] if (arr[index] - target) > (target - arr[index - 1]) else arr[index]
    
    def get_closest_three(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append(arr[index - 1])
        if index < len(arr):
            candidates.append(arr[index])
        if index + 1 < len(arr):
            candidates.append(arr[index + 1])
        return candidates
    
    def get_closest_three_values(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append(arr[index - 1])
        if index < len(arr):
            candidates.append(arr[index])
        if index + 1 < len(arr):
            candidates.append(arr[index + 1])
        return candidates
    
    def get_closest_three_values_with_indices(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1))
        if index < len(arr):
            candidates.append((arr[index], index))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1))
        return candidates
    
    def get_closest_three_values_with_indices_and_values(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1))
        if index < len(arr):
            candidates.append((arr[index], index))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target)))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target)))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target)))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1]))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index]))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1]))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1]))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index]))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1]))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1], target))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index], target))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1], target))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets_and_values(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1], target, arr[index - 1]))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index], target, arr[index]))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1], target, arr[index + 1]))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets_and_values_and_targets(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1], target, arr[index - 1], target))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index], target, arr[index], target))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1], target, arr[index + 1], target))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets_and_values_and_targets_and_values(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1], target, arr[index - 1], target, arr[index - 1]))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index], target, arr[index], target, arr[index]))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1], target, arr[index + 1], target, arr[index + 1]))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets_and_values_and_targets_and_values_and_targets(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1], target, arr[index - 1], target, arr[index - 1], target))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index], target, arr[index], target, arr[index], target))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1], target, arr[index + 1], target, arr[index + 1], target))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets_and_values_and_targets_and_values_and_targets_and_values(arr, target):
        index = bisect.bisect_left(arr, target)
        candidates = []
        if index > 0:
            candidates.append((arr[index - 1], index - 1, abs(arr[index - 1] - target), arr[index - 1], target, arr[index - 1], target, arr[index - 1], target, arr[index - 1]))
        if index < len(arr):
            candidates.append((arr[index], index, abs(arr[index] - target), arr[index], target, arr[index], target, arr[index], target, arr[index]))
        if index + 1 < len(arr):
            candidates.append((arr[index + 1], index + 1, abs(arr[index + 1] - target), arr[index + 1], target, arr[index + 1], target, arr[index + 1], target, arr[index + 1]))
        return candidates
    
    def get_closest_three_values_with_indices_and_values_and_distances_and_targets_and_values_and_targets_and_values_and_targets_and_values_and_targets_and_values_and_targets(arr, target):
        index = bisect.bisect

check(find_three_closest_elements)