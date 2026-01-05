import sys

def solve():
    import sys
    S = sys.stdin.buffer.read().decode().strip()
    max_num = -1
    n = len(S)
    
    for i in range(n):
        for j in range(i, n):
            substr = S[i:j+1]
            # Try changing at most one letter to a digit
            # We can try changing each letter to a digit from 0-9
            # Also consider the original substring if it's all digits
            # Check if the substring has any letters
            has_letter = any(c.isalpha() for c in substr)
            if not has_letter:
                # All digits, check if it's larger than current max
                num = int(substr)
                if num > max_num:
                    max_num = num
                continue
            # Try changing each letter to a digit
            for k in range(len(substr)):
                if substr[k].isalpha():
                    # Try changing this character to a digit 0-9
                    for d in range(10):
                        new_substr = substr[:k] + str(d) + substr[k+1:]
                        # Check if new_substr is all digits
                        if all(c.isdigit() for c in new_substr):
                            num = int(new_substr)
                            if num > max_num:
                                max_num = num
    print(max_num)

if __name__ == '__main__':
    solve()