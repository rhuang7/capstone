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
        final_x, final_y = 0, 0
        
        for c in s:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
        final_x, final_y = x, y
        
        x, y = 0, 0
        count = 0
        
        for c in s:
            if c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            elif c == 'L':
                x -= 1
            elif c == 'R':
                x += 1
            if x == final_x and y == final_y:
                count += 1
        
        print(N - count)

if __name__ == '__main__':
    solve()