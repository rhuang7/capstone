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
            # Check if the substring has any letters
            letters = [c for c in substr if c.isalpha()]
            if len(letters) > 1:
                continue
            # Try changing the letter to a digit
            if letters:
                for c in '0123456789':
                    new_sub = substr.replace(letters[0], c)
                    if new_sub.isdigit():
                        num = int(new_sub)
                        if num > max_num:
                            max_num = num
            else:
                num = int(substr)
                if num > max_num:
                    max_num = num
    print(max_num)

if __name__ == '__main__':
    solve()