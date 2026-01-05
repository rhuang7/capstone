import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        S = data[index + 1]
        index += 2
        
        from collections import Counter
        
        count = Counter(S)
        odd_count = 0
        
        for char, freq in count.items():
            if freq % 2 != 0:
                odd_count += 1
        
        if odd_count > 2:
            print("NO")
            continue
        
        # Check if the string can be rearranged into a doublindrome
        # A doublindrome requires that each half is a palindrome
        # So, for each character, its frequency must be even (or at most two characters with odd counts)
        # But since N is even, we can have at most two characters with odd counts
        
        # Now check if the string can be rearranged into a doublindrome
        # We can do this by checking if the frequency of each character is even or at most 2 characters have odd counts
        
        # For a doublindrome, each half must be a palindrome
        # So, each half must have even counts for all characters
        # So, the total count of each character must be even
        
        # So, we need to check if all characters have even counts
        # Or, if exactly two characters have odd counts (which can be split into two halves)
        
        # So, for the string to be rearranged into a doublindrome, the count of characters with odd frequency must be <= 2
        
        # But since N is even, we can have at most two characters with odd counts
        
        # So, the condition is already satisfied if odd_count <= 2
        
        # Now, we need to check if the string can be rearranged into a doublindrome
        # For that, the frequency of each character must be even (so that it can be split into two halves)
        # Or, exactly two characters have odd counts (so that they can be split into two halves)
        
        # So, the condition is that the number of characters with odd counts is <= 2
        
        # But since N is even, we can have at most two characters with odd counts
        
        # So, the answer is YES if the number of characters with odd counts is <= 2
        
        # But we need to check if the string can be rearranged into a doublindrome
        # For that, each half must be a palindrome
        # So, the frequency of each character must be even (so that it can be split into two halves)
        # Or, exactly two characters have odd counts (so that they can be split into two halves)
        
        # So, the condition is that the number of characters with odd counts is <= 2
        
        # But since N is even, we can have at most two characters with odd counts
        
        # So, the answer is YES if the number of characters with odd counts is <= 2
        
        # But we need to check if the string can be rearranged into a doublindrome
        # For that, the frequency of each character must be even (so that it can be split into two halves)
        # Or, exactly two characters have odd counts (so that they can be split into two halves)
        
        # So, the condition is that the number of characters with odd counts is <= 2
        
        # But since N is even, we can have at most two characters with odd counts
        
        # So, the answer is YES if the number of characters with odd counts is <= 2
        
        # So, we can just check if the number of characters with odd counts is <= 2
        
        if odd_count <= 2:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()