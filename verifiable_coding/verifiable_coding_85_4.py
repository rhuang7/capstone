import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        s = data[index]
        index += 1
        x = int(data[index])
        index += 1
        
        n = len(s)
        w = ['0'] * n
        
        for i in range(n):
            if s[i] == '1':
                # Check if w[i - x] is 1 (i > x)
                if i > x and w[i - x] == '1':
                    continue
                # Check if w[i + x] is 1 (i + x <= n)
                if i + x < n and w[i + x] == '1':
                    continue
                # If neither condition is met, set w[i] to 1
                w[i] = '1'
        
        # Check if the constructed w produces the given s
        valid = True
        for i in range(n):
            s_i = s[i]
            if s_i == '1':
                # Check if w[i - x] is 1 (i > x)
                if i > x and w[i - x] == '1':
                    continue
                # Check if w[i + x] is 1 (i + x <= n)
                if i + x < n and w[i + x] == '1':
                    continue
                # If neither condition is met, it's invalid
                valid = False
                break
            else:
                # Check if both conditions are false
                if (i > x and w[i - x] == '1') or (i + x < n and w[i + x] == '1'):
                    valid = False
                    break
        
        if valid:
            print(''.join(w))
        else:
            print(-1)

if __name__ == '__main__':
    solve()