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
                # Check if w[i - x] exists and is 1
                if i - x >= 0 and w[i - x] == '1':
                    continue
                # Check if w[i + x] exists and is 1
                if i + x < n and w[i + x] == '1':
                    continue
                # If neither, then it's invalid
                print(-1)
                break
        else:
            # If we reached here, all characters are valid
            print(''.join(w))
            
if __name__ == '__main__':
    solve()