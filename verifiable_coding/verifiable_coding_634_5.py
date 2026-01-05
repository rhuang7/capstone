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
            for k in range(len(substring)):
                if substring[k].isdigit():
                    continue
                # Try changing to each digit 0-9
                for d in range(10):
                    new_sub = substring[:k] + str(d) + substring[k+1:]
                    num = int(new_sub)
                    if num > max_num:
                        max_num = num
    print(max_num)

if __name__ == '__main__':
    solve()