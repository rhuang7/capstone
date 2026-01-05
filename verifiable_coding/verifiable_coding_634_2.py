import sys

def solve():
    import sys
    S = sys.stdin.buffer.read().decode().strip()
    max_num = -1
    n = len(S)
    
    for i in range(n):
        for j in range(i, n):
            substring = S[i:j+1]
            # Try changing each character in the substring to a digit if it's a letter
            for k in range(i, j+1):
                if substring[k].isalpha():
                    for d in range(10):
                        new_sub = substring[:k] + str(d) + substring[k+1:]
                        num = int(new_sub)
                        if num > max_num:
                            max_num = num
                else:
                    # No change needed, just check the current substring
                    num = int(substring)
                    if num > max_num:
                        max_num = num
    print(max_num)

if __name__ == '__main__':
    solve()