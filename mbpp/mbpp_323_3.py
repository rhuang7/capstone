def check(candidate):
    assert candidate([-5, -2, 5, 2, 4,	7, 1, 8, 0, -8], 10) == [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
    assert candidate([1, 2, 3, -4, -1, 4], 6) == [-4, 1, -1, 2, 3, 4]
    assert candidate([4, 7, 9, 77, -4, 5, -3, -9], 8) == [-4, 4, -3, 7, -9, 9, 77, 5]


def rearrange_alternating(arr):
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]
    
    result = []
    i = j = 0
    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        result.append(negatives[j])
        i += 1
        j += 1
    
    while i < len(positives):
        result.append(positives[i])
        i += 1
    
    while j < len(negatives):
        result.append(negatives[j])
        j += 1
    
    return result

check(rearrange_alternating)