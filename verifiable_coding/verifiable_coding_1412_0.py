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
            line = data[idx].split()
            idx += 1
            ci = line[0].decode()
            pi = line[1].decode()
            rules[ci] = pi
        while idx < len(data) and data[idx] == b'':
            idx += 1
        if idx >= len(data):
            S = b''
        else:
            S = data[idx].decode()
            idx += 1
        # Apply rules
        encrypted = S
        for ci in rules:
            encrypted = encrypted.replace(ci, rules[ci])
        # Process the number
        # Split into integer and fractional parts
        parts = encrypted.split('.')
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else ''
        # Remove leading and trailing zeros
        integer_part = integer_part.rstrip('0')
        fractional_part = fractional_part.rstrip('0')
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