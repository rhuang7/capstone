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
        for i in range(n):
            if i == 0:
                # First digit is 2, so a and b must be 1 and 1 (1+1=2)
                a.append('1')
                b.append('1')
            else:
                # For other digits, we want to minimize max(a, b)
                # So we try to make a and b as small as possible
                # Try to set a[i] = 0, b[i] = x[i]
                # If that's not possible (because x[i] is 2, then a[i] and b[i] must be 1 and 1)
                # Or if x[i] is 1, then a[i] and b[i] can be 0 and 1 or 1 and 0
                # We choose the option that makes a and b as small as possible
                if x[i] == '2':
                    a.append('1')
                    b.append('1')
                else:
                    # Try to make a[i] = 0, b[i] = x[i]
                    # If x[i] is 1, then a[i] = 0 and b[i] = 1
                    # If x[i] is 0, then a[i] = 0 and b[i] = 0
                    a.append('0')
                    b.append(x[i])
        
        print(''.join(a))
        print(''.join(b))
        
if __name__ == '__main__':
    solve()