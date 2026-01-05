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
            encrypted = encrypted.replace(c.encode(), rules[c].encode())
        
        # Convert to string
        s = encrypted.decode()
        
        # Process the string as a decimal number
        s = s.replace(' ', '')
        if '.' in s:
            parts = s.split('.')
            integral = parts[0]
            fractional = parts[1]
        else:
            integral = s
            fractional = ''
        
        # Remove leading and trailing zeros
        integral = integral.lstrip('0')
        fractional = fractional.rstrip('0')
        
        # Handle edge cases
        if integral == '':
            integral = '0'
        if fractional == '':
            result = integral
        else:
            result = f"{integral}.{''.join(fractional)}" if integral else f".{fractional}"
        
        # Remove leading zero if integral part is zero and fractional part is non-zero
        if integral == '0' and fractional:
            result = f".{fractional}"
        
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()