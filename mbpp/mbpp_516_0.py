def check(candidate):
    assert candidate([15, 79, 25, 68, 37]) == [15, 25, 37, 68, 79]
    assert candidate([9, 11, 8, 7, 3, 2]) == [2, 3, 7, 8, 9, 11]
    assert candidate([36, 12, 24, 26, 29]) == [12, 24, 26, 29, 36]


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr) if arr else 0
    # Get the number of digits in the maximum number
    max_digits = len(str(max_num))
    
    # Initialize buckets for each digit (0-9)
    buckets = [[] for _ in range(10)]
    
    # Iterate over each digit position
    for digit in range(max_digits):
        # Distribute numbers into buckets based on the current digit
        for num in arr:
            # Extract the current digit
            current_digit = (num // (10 ** digit)) % 10
            buckets[current_digit].append(num)
        # Collect the numbers from the buckets in order
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        # Reset buckets for the next digit
        buckets = [[] for _ in range(10)]
    
    return arr

check(radix_sort)