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
        encrypted = encrypted.decode()
        
        # Process the number
        parts = encrypted.split('.')
        if len(parts) == 1:
            integer_part = parts[0]
            fractional_part = ''
        else:
            integer_part = parts[0]
            fractional_part = parts[1]
        
        # Remove leading and trailing zeros
        integer_part = integer_part.lstrip('0')
        if integer_part == '':
            integer_part = '0'
        
        fractional_part = fractional_part.rstrip('0')
        
        # Build result
        result = ''
        if integer_part != '0':
            result += integer_part
        if fractional_part:
            if integer_part != '0':
                result += '.'
            result += fractional_part
        else:
            if integer_part == '0':
                result = '.0'
        
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()