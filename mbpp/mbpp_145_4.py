def check(candidate):
    assert candidate((2,1,5,3),4) == 4
    assert candidate((9,3,2,5,1),5) == 8
    assert candidate((3,2,1),3) == 2


def max_difference(arr):
    if not arr or len(arr) < 2:
        return 0  # or raise ValueError depending on requirements
    
    min_val = arr[0]
    max_diff = 0
    
    for num in arr:
        if num < min_val:
            min_val = num
        else:
            current_diff = num - min_val
            if current_diff > max_diff:
                max_diff = current_diff
                
    return max_diff

check(max_difference)