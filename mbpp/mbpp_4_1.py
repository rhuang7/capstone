def check(candidate):
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65] 
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75] 
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]


import heapq

def find_largest_numbers(numbers, k):
    if not numbers or k <= 0:
        return []
    return heapq.nlargest(k, numbers)

check(find_largest_numbers)