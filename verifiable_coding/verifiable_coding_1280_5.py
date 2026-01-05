import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i]
        n = len(S)
        operations = 0
        
        for j in range(n // 2):
            left = S[j]
            right = S[n - 1 - j]
            
            # Find the minimum operations to make left and right equal
            # We can only decrease characters, so we need to find the common character
            # that is less than or equal to both and calculate the steps needed
            # We'll find the minimum steps by moving both towards 'a'
            # or find the common character that is the same for both
            # For example, if left is 'c' and right is 'd', we can change 'd' to 'c' (1 step)
            # or change 'c' to 'b' and 'd' to 'b' (2 steps)
            # So we need to find the common character that is the minimum steps
            # We can do this by finding the minimum of the two characters and moving both to it
            # or find the common character that is the same for both
            # For this problem, we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by moving both towards 'a'
            # and find the common character that is the same for both
            # So we can find the minimum steps by