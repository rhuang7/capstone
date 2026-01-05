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
            # If digit is 0, then a=0 and b=0 (0+0=0)
            # If digit is 1, then a=0 and b=1 (0+1=1)
            # If digit is 2, then a=0 and b=2 (0+2=2)
            # But we want to minimize max(a, b), so we try to make a as small as possible
            # So we try to make a as small as possible, and b as large as possible
            # So we try to assign a as 0 and b as digit, but if that makes a smaller than b, we swap
            # But we have to make sure that a and b do not have leading zeros
            # So we try to assign a as 0 and b as digit, and then check if that is possible
            # If it is possible, we do that, else we assign a as digit and b as 0
            
            # Try to assign a as 0 and b as digit
            a_digit = 0
            b_digit = digit
            
            # Check if this assignment is valid
            # a and b must not have leading zeros
            # Since we are starting from the second digit, leading zeros are allowed
            # So this assignment is valid
            
            a.append(str(a_digit))
            b.append(str(b_digit))
        
        # Now, we have a and b, but we need to make sure that max(a, b) is minimized
        # So we need to make a and b as small as possible
        # So we need to make a as small as possible and b as small as possible
        # But we have to make sure that a and b are not leading zeros
        # So we need to make sure that the first digit is 1 (since it's guaranteed to be 2)
        # So the first digit is already 1 for both a and b
        
        # Now, we need to make sure that a and b are as small as possible
        # So we need to make a as small as possible and b as small as possible
        # So we need to make a and b as small as possible
        # So we need to make a and b as small as possible, but without leading zeros
        # So we need to make a and b as small as possible
        
        # So we can just print a and b as they are
        
        print(''.join(a))
        print(''.join(b))
        
if __name__ == '__main__':
    solve()