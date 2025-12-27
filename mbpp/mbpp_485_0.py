def check(candidate):
    assert candidate([1, 232, 54545, 999991], 4) == 54545
    assert candidate([1, 2, 3, 4, 5, 50], 6) == 5
    assert candidate([1, 3, 7, 9, 45], 5)  == 9


def find_largest_palindromic_number(arr):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    palindromes = [num for num in arr if is_palindrome(num)]
    
    if not palindromes:
        return None
    
    return max(palindromes)

check(find_largest_palindromic_number)