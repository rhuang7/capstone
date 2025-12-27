def check(candidate):
    assert candidate(10)==[1, 3, 7, 9, 13, 15, 21, 25, 31, 33] 
    assert candidate(5)==[1, 3, 7, 9, 13]
    assert candidate(8)==[1, 3, 7, 9, 13, 15, 21, 25]


def print_lucky_numbers(n):
    if n <= 0:
        return
    
    # Initialize the list of lucky numbers with the first number
    lucky = [1]
    
    # The maximum number to check up to
    max_num = 2 * n
    
    for i in range(2, max_num + 1):
        # Check if i is lucky
        is_lucky = True
        for num in lucky:
            if i % num == 0:
                is_lucky = False
                break
        if is_lucky:
            lucky.append(i)
    
    # Print the first n lucky numbers
    for num in lucky[:n]:
        print(num)

check(print_lucky_numbers)