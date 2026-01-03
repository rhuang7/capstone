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
        
        # First digit is 2, so a and b must be 1 and 1 (since 1+1=2 mod 3)
        a.append('1')
        b.append('1')
        
        for i in range(1, n):
            digit = int(x[i])
            
            # Try to assign 0 to a and digit to b
            # If digit is 0, then a can be 0 and b can be 0
            # If digit is 1, then a can be 0 and b can be 1
            # If digit is 2, then a can be 0 and b can be 2
            # But we want to minimize max(a, b), so we try to make a as small as possible
            # So we try to make a as 0 as possible, and b as digit as possible
            # But if we make a 0, then b is digit, but if we make a 1, then b is (digit - 1) mod 3
            # We need to choose the option that makes max(a, b) as small as possible
            # So we try to make a as small as possible, and b as small as possible
            
            # Try to make a as 0 as possible
            # So try to make a = 0, b = digit
            # But if digit is 2, then a can be 0 and b can be 2
            # But if digit is 2, then a can be 1 and b can be 1 (since 1+1=2 mod 3)
            # So we need to choose between (a=0, b=digit) and (a=1, b=(digit - 1) % 3)
            # We want to choose the option that makes max(a, b) as small as possible
            
            # Try both options and choose the one with smaller max(a, b)
            # Option 1: a = 0, b = digit
            # Option 2: a = 1, b = (digit - 1) % 3
            
            option1 = (0, digit)
            option2 = (1, (digit - 1) % 3)
            
            max1 = max(option1)
            max2 = max(option2)
            
            if max1 <= max2:
                a.append('0')
                b.append(str(digit))
            else:
                a.append('1')
                b.append(str((digit - 1) % 3))
        
        print(''.join(a))
        print(''.join(b))

if __name__ == '__main__':
    solve()