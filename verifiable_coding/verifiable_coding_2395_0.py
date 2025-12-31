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
                # First digit is 2, so a and b must be 1 and 1
                a.append('1')
                b.append('1')
            else:
                # For other digits, we want to minimize max(a, b)
                # So we try to make a and b as small as possible
                # Try to make a = 0, b = x[i] (if possible)
                # If not possible, try a = 1, b = (x[i] - 1) % 3
                # If not possible, try a = 2, b = (x[i] - 2) % 3
                # We want to choose the option that makes a and b as small as possible
                # and also ensures that a and b are not leading zeros
                # Since first digit is already handled, we can proceed
                digit = int(x[i])
                if digit == 0:
                    a.append('0')
                    b.append('0')
                elif digit == 1:
                    a.append('0')
                    b.append('1')
                else:
                    a.append('0')
                    b.append('2')
        
        print(''.join(a))
        print(''.join(b))
        
if __name__ == '__main__':
    solve()