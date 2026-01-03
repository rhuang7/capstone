import sys

def solve():
    import sys
    S = sys.stdin.buffer.read().decode().strip()
    max_num = -1
    n = len(S)
    
    for i in range(n):
        for j in range(i, n):
            substring = S[i:j+1]
            # Try changing at most one letter to a digit
            for k in range(i, j+1):
                if substring[k].isdigit():
                    continue
                # Try changing this character to a digit (0-9)
                for d in range(10):
                    new_substring = substring[:k] + str(d) + substring[k+1:]
                    num = int(new_substring)
                    if num > max_num:
                        max_num = num
            # Try the original substring (no changes)
            num = int(substring)
            if num > max_num:
                max_num = num
    print(max_num)

if __name__ == '__main__':
    solve()