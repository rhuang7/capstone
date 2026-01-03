import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        s = data[i]
        n = len(s)
        left = 0
        right = n - 1
        
        # Find the first mismatch
        while left < right:
            if s[left] != s[right]:
                # Check if deleting left or right character makes it a palindrome
                # Check deleting left
                flag1 = True
                temp_left = left + 1
                temp_right = right
                while temp_left < temp_right:
                    if s[temp_left] != s[temp_right]:
                        flag1 = False
                        break
                    temp_left += 1
                    temp_right -= 1
                if flag1:
                    results.append("YES")
                    break
                # Check deleting right
                flag2 = True
                temp_left = left
                temp_right = right - 1
                while temp_left < temp_right:
                    if s[temp_left] != s[temp_right]:
                        flag2 = False
                        break
                    temp_left += 1
                    temp_right -= 1
                if flag2:
                    results.append("YES")
                    break
                # If neither works, it's not possible
                results.append("NO")
                break
            left += 1
            right -= 1
        else:
            # If the entire string is a palindrome, deleting one character will still leave it a palindrome
            results.append("YES")
    
    print('\n'.join(results))