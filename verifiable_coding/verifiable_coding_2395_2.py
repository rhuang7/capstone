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
        
        # The first digit of x is 2, so a[0] + b[0] % 3 = 2
        # To minimize max(a, b), we want a[0] and b[0] to be as small as possible
        # So we set a[0] = 1, b[0] = 1 (1 + 1 = 2)
        a.append('1')
        b.append('1')
        
        for i in range(1, n):
            digit = int(x[i])
            # We want to choose a[i] and b[i] such that (a[i] + b[i]) % 3 = digit
            # To minimize max(a, b), we want a[i] and b[i] to be as small as possible
            # So we set a[i] = 0, b[i] = digit (if digit is 0 or 1)
            # Or a[i] = 1, b[i] = (digit - 1) % 3 (if digit is 2)
            if digit == 0:
                a.append('0')
                b.append('0')
            elif digit == 1:
                a.append('0')
                b.append('1')
            else:  # digit == 2
                a.append('1')
                b.append('1')
        
        print(''.join(a))
        print(''.join(b))
        
if __name__ == '__main__':
    solve()