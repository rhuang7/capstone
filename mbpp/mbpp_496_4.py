def check(candidate):
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 25, 58],3)==[14, 22, 25] 
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 25, 58],2)==[14, 22]
    assert candidate( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[14, 22, 22, 25, 35]


import heapq

def find_smallest_numbers(nums, k):
    return heapq.nsmallest(k, nums)

check(find_smallest_numbers)