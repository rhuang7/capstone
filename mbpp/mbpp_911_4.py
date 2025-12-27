def check(candidate):
    assert candidate( [12, 74, 9, 50, 61, 41])==225700
    assert candidate([25, 35, 22, 85, 14, 65, 75, 25, 58])==414375
    assert candidate([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==2520


import heapq

def max_product_of_three(nums):
    # Create a max heap of the three largest numbers
    heapq._heapify_max(nums)
    largest_three = [nums[0], nums[1], nums[2]]
    
    # Create a min heap of the three smallest numbers
    heapq.heapify(nums)
    smallest_three = [nums[0], nums[1], nums[2]]
    
    # Compute the product of the three largest numbers
    product1 = largest_three[0] * largest_three[1] * largest_three[2]
    
    # Compute the product of the two smallest (negative) and the largest number
    product2 = smallest_three[0] * smallest_three[1] * largest_three[2]
    
    # Return the maximum of the two products
    return max(product1, product2)

check(max_product_of_three)