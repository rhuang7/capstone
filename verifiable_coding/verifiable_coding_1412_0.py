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
            ci, pi = line[0], line[1]
            rules[ci] = pi
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
        encrypted_str = encrypted.decode()
        # Process the number
        # Split into integer and fractional parts
        if '.' in encrypted_str:
            int_part, frac_part = encrypted_str.split('.', 1)
        else:
            int_part = encrypted_str
            frac_part = ''
        # Remove leading and trailing zeros
        int_part = int_part.lstrip('0')
        frac_part = frac_part.rstrip('0')
        # Handle edge cases
        if int_part == '':
            int_part = '0'
        if frac_part == '':
            result = int_part
        else:
            result = f"{int_part}.{frac_part}" if int_part != '0' else frac_part
        # Special case for 0.0
        if result == '0.0':
            result = '0'
        results.append(result)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()