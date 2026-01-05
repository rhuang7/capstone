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
        # Process the string to get the shortest notation
        # Split into integer and fractional parts
        if '.' in s:
            integer_part, fractional_part = s.split('.', 1)
        else:
            integer_part = s
            fractional_part = ''
        # Remove leading and trailing zeros
        integer_part = integer_part.lstrip('0')
        fractional_part = fractional_part.rstrip('0')
        # Handle edge cases
        if integer_part == '':
            integer_part = '0'
        if fractional_part == '':
            fractional_part = ''
        # Combine parts
        if fractional_part:
            if integer_part == '0':
                result = f'.{fractional_part}'
            else:
                result = f'{integer_part}.{fractional_part}'
        else:
            result = integer_part
        results.append(result)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()