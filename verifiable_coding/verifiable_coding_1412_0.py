import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
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
            ci, pi = data[idx].split()
            rules[ci] = pi
            idx += 1
        while idx < len(data) and data[idx] == b'':
            idx += 1
        if idx >= len(data):
            S = b''
        else:
            S = data[idx]
            idx += 1
        # Apply rules
        encrypted = S
        for ci in rules:
            encrypted = encrypted.replace(ci, rules[ci].encode())
        # Convert to string
        s = encrypted.decode()
        # Process the string as a number
        # Split into integer and fractional parts
        if '.' in s:
            int_part, frac_part = s.split('.', 1)
        else:
            int_part = s
            frac_part = ''
        # Remove leading and trailing zeros
        int_part = int_part.lstrip('0')
        frac_part = frac_part.rstrip('0')
        # Handle empty parts
        if int_part == '':
            int_part = '0'
        if frac_part == '':
            frac_part = ''
        # Construct the result
        if int_part == '0' and frac_part == '':
            results.append('0')
        elif int_part == '0':
            results.append('.' + frac_part)
        else:
            results.append(int_part + ('.' + frac_part if frac_part else ''))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()