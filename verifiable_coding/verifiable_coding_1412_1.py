import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        while idx < len(data) and data[idx] == b'':
            idx += 1
        if idx >= len(data):
            break
        N = int(data[idx])
        idx += 1
        rules = {}
        for _ in range(N):
            while idx < len(data) and data[idx] == b'':
                idx += 1
            if idx >= len(data):
                break
            line = data[idx].split()
            idx += 1
            ci, pi = line[0], line[1]
            rules[ci] = pi
        while idx < len(data) and data[idx] == b'':
            idx += 1
        if idx >= len(data):
            S = b''
        else:
            S = data[idx]
            idx += 1
        encrypted = S.decode()
        replaced = []
        for c in encrypted:
            if c in rules:
                replaced.append(rules[c])
            else:
                replaced.append(c)
        password = ''.join(replaced)
        parts = password.split('.')
        if len(parts) == 1:
            integer_part = parts[0]
            fractional_part = ''
        else:
            integer_part = parts[0]
            fractional_part = parts[1]
        integer_part = integer_part.lstrip('0')
        if integer_part == '':
            integer_part = '0'
        fractional_part = fractional_part.rstrip('0')
        if fractional_part == '':
            result = integer_part
        else:
            result = f"{integer_part}.{fractional_part}" if integer_part != '0' else f".{fractional_part}"
        print(result)

if __name__ == '__main__':
    solve()