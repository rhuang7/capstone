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
        
        # First digit is 2, so a and b must be 1 and 1 (1+1=2 mod 3)
        a.append('1')
        b.append('1')
        
        for i in range(1, n):
            digit = int(x[i])
            if digit == 0:
                # a and b must be 0 and 0 (0+0=0 mod 3)
                a.append('0')
                b.append('0')
            elif digit == 1:
                # a and b can be 0 and 1 or 1 and 0
                # To minimize max(a, b), we choose 0 and 1
                a.append('0')
                b.append('1')
            else:  # digit == 2
                # a and b must be 1 and 1 (1+1=2 mod 3)
                a.append('1')
                b.append('1')
        
        print(''.join(a))
        print(''.join(b))

if __name__ == '__main__':
    solve()