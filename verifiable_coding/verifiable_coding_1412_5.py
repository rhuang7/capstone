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
            c, p = data[idx].split()
            rules[c] = p
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
        for c in rules:
            encrypted = encrypted.replace(c, rules[c].encode())
        # Convert to string
        s = encrypted.decode()
        # Process the string as a number
        # Split into integer and fractional parts
        if '.' in s:
            integer_part, fractional_part = s.split('.', 1)
        else:
            integer_part = s
            fractional_part = ''
        # Remove leading and trailing zeros
        integer_part = integer_part.rstrip('0')
        fractional_part = fractional_part.lstrip('0')
        # Handle cases
        if integer_part == '' and fractional_part == '':
            results.append('0')
        elif integer_part == '':
            results.append('.' + fractional_part)
        elif fractional_part == '':
            results.append(integer_part)
        else:
            results.append(integer_part + '.' + fractional_part)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()