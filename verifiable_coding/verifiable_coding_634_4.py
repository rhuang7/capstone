import sys

def solve():
    import sys
    S = sys.stdin.buffer.read().decode().strip()
    max_num = -1
    n = len(S)
    for i in range(n):
        for j in range(i, n):
            substr = S[i:j+1]
            cnt = 0
            for c in substr:
                if c.isalpha():
                    cnt += 1
            if cnt > 1:
                continue
            if cnt == 1:
                new_str = list(substr)
                for k in range(26):
                    new_str[0] = str(k)
                    new_sub = ''.join(new_str)
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