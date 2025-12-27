def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 3, 2], 7) == 6
    assert candidate([10, 9, 4, 5, 4, 8, 6], 7) == 3
    assert candidate([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7


def longest_consecutive_subsequence(arr):
    if not arr:
        return []
    
    # Create a set for O(1) lookups
    num_set = set(arr)
    max_length = 0
    start = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Expand the sequence as far as possible
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            # Update max_length and start if needed
            if current_length > max_length:
                max_length = current_length
                start = num
    
    # Return the subsequence
    return list(range(start, start + max_length))

check(longest_consecutive_subsequence)