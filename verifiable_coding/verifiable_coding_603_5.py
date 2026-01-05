import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    K_list = list(map(int, input[1:T+1]))
    
    for K in K_list:
        if K == 0:
            print('a')
            continue
        # Create a string with K "drops" (a > b > c > ... > z)
        # The minimal length is K + 1, as each drop requires at least two characters
        # To make the lex smallest, we use the largest possible letters in the earliest positions
        # So we start from 'z' and go backwards
        res = []
        current = 'z'
        for i in range(K + 1):
            res.append(current)
            current = chr(ord(current) - 1)
        print(''.join(res))
        
if __name__ == '__main__':
    solve()