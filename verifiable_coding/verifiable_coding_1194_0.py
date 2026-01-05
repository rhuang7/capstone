import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        x, y = 0, 0
        dest_x, dest_y = 0, 0
        
        for c in s:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
        dest_x, dest_y = x, y
        
        x, y = 0, 0
        removed = 0
        
        for c in s:
            if c == 'U':
                if y < dest_y:
                    y += 1
                else:
                    removed += 1
            elif c == 'D':
                if y > dest_y:
                    y -= 1
                else:
                    removed += 1
            elif c == 'L':
                if x < dest_x:
                    x -= 1
                else:
                    removed += 1
            elif c == 'R':
                if x > dest_x:
                    x += 1
                else:
                    removed += 1
        
        print(removed)

if __name__ == '__main__':
    solve()