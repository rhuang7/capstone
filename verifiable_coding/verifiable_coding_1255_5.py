import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        s = data[index]
        k = int(data[index + 1])
        index += 2
        
        used = set(s)
        unique_chars = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in used]
        unique_chars.sort()
        
        # Calculate the number of characters in s
        n = len(s)
        
        # If k is greater than or equal to n, then the answer is the lex smallest string with unique chars
        if k >= n:
            print(''.join(unique_chars))
            continue
        
        # We need to choose (n - k) characters from the unique_chars to avoid matching s
        # The rest will be from the used characters
        # We want the lex smallest string, so we need to choose the smallest possible characters
        # to avoid matching s
        
        # Get the characters in s sorted
        s_sorted = sorted(s)
        
        # We need to choose (n - k) characters from unique_chars to avoid matching s
        # The rest will be from s_sorted, but we need to choose the smallest possible
        # to make the overall string lex smallest
        
        # The lex smallest string will have the smallest possible characters not in s
        # and the smallest possible characters in s that are not matched
        
        # We can use a greedy approach:
        # 1. Take the smallest (n - k) characters not in s
        # 2. Take the remaining characters from s, but in sorted order
        
        # Get the characters not in s
        not_in_s = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in used]
        not_in_s_sorted = sorted(not_in_s)
        
        # Take the first (n - k) characters from not_in_s_sorted
        not_in_s_selected = not_in_s_sorted[:n - k]
        
        # The remaining k characters will be from s_sorted, but we need to choose the smallest possible
        # to make the overall string lex smallest
        
        # Take the first k characters from s_sorted
        s_selected = s_sorted[:k]
        
        # Combine the two lists and sort them to get the lex smallest string
        result = sorted(not_in_s_selected + s_selected)
        print(''.join(result))
        
if __name__ == '__main__':
    solve()