import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        s = data[idx]
        idx += 1
        x = int(data[idx])
        idx += 1
        
        n = len(s)
        w = ['0'] * n
        
        for i in range(n):
            if s[i] == '1':
                # Check if w[i - x] exists and is 1
                if i - x >= 0 and w[i - x] == '1':
                    w[i] = '1'
                # Check if w[i + x] exists and is 1
                elif i + x < n and w[i + x] == '1':
                    w[i] = '1'
                else:
                    # If both conditions are false, then s[i] should be 0
                    # But since s[i] is 1, this is invalid
                    print(-1)
                    break
        else:
            print(''.join(w))
            continue
        print(-1)

if __name__ == '__main__':
    solve()