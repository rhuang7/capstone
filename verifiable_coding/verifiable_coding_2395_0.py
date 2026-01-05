import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        x = data[index]
        index += 1
        
        a = []
        b = []
        
        # First digit is 2, so a[0] + b[0] mod 3 = 2
        # To minimize max(a, b), we want a and b to be as small as possible
        # So we set a[0] = 1, b[0] = 1 (1 + 1 = 2 mod 3)
        a.append('1')
        b.append('1')
        
        for i in range(1, n):
            digit = int(x[i])
            # For each digit, we want to choose a[i] and b[i] such that (a[i] + b[i]) % 3 = digit
            # To minimize max(a, b), we try to make a[i] and b[i] as small as possible
            # We try to set a[i] = 0, then b[i] = digit (if digit is 0 or 1)
            # If digit is 2, then a[i] = 1, b[i] = 1
            # If digit is 1, then a[i] = 0, b[i] = 1
            # If digit is 0, then a[i] = 0, b[i] = 0
            # But we need to ensure that a and b do not have leading zeros
            # So we need to check if we can set a[i] = 0 and b[i] = digit
            # If that is not possible (e.g. digit is 2), then we set a[i] = 1, b[i] = 1
            # But we also need to ensure that a and b do not have leading zeros
            # So we need to check if the current digit is 2, then we have to set a[i] = 1, b[i] = 1
            # Otherwise, we can set a[i] = 0, b[i] = digit
            if digit == 2:
                a.append('1')
                b.append('1')
            else:
                a.append('0')
                b.append(str(digit))
        
        print(''.join(a))
        print(''.join(b))

if __name__ == '__main__':
    solve()