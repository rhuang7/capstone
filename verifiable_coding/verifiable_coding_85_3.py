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
                # Check if w[i - x] is 1 and i > x
                if i > x and w[i - x] == '1':
                    w[i] = '1'
                # Check if w[i + x] is 1 and i + x <= n
                elif i + x < n and w[i + x] == '1':
                    w[i] = '1'
                else:
                    # This means the current position in s is 1 but neither condition is met
                    # So it's impossible to reconstruct w
                    print(-1)
                    break
        else:
            print(''.join(w))
            
if __name__ == '__main__':
    solve()