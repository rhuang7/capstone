import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    first_line = input[0]
    T_str, M = first_line.decode().split()
    T = int(T_str)
    M = M
    mapping = {chr(ord('a') + i): M[i] for i in range(26)}
    upper_mapping = {chr(ord('A') + i): M[i].upper() for i in range(26)}
    for line in input[1:T+1]:
        s = line.decode()
        res = []
        for c in s:
            if c == '_':
                res.append(' ')
            elif c.isalpha():
                if c.isupper():
                    res.append(upper_mapping[c.lower()])
                else:
                    res.append(mapping[c])
            else:
                res.append(c)
        print(''.join(res))

if __name__ == '__main__':
    solve()