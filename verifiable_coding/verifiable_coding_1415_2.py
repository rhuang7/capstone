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
                # Check if skipping left or right gives a palindrome
                skip_left = s[left + 1:right + 1] == s[left + 1:right + 1][::-1]
                skip_right = s[left:right] == s[left:right][::-1]
                if skip_left or skip_right:
                    results.append("YES")
                else:
                    results.append("NO")
                break
            left += 1
            right -= 1
        else:
            # Already a palindrome, but we need to delete exactly one character
            results.append("YES")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()