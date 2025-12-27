def check(candidate):
    assert candidate("11000010001", 11) == 6
    assert candidate("10111", 5) == 1
    assert candidate("11011101100101", 14) == 2 


def max_diff_in_substring(binary_str):
    min_sum = 0
    current_sum = 0
    max_diff = float('-inf')
    
    for char in binary_str:
        current_sum += 1 if char == '1' else -1
        
        if current_sum < min_sum:
            min_sum = current_sum
        
        max_diff = max(max_diff, current_sum - min_sum)
    
    return max_diff if max_diff != float('-inf') else 0

check(max_diff_in_substring)