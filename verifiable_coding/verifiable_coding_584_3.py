import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    strings = data[1:N+1]
    
    for s in strings:
        max_circles = 0
        current_size = 0
        is_square = True
        
        for c in s:
            if c == '1':
                if is_square:
                    current_size = 1
                    is_square = False
                else:
                    if current_size % 2 == 0:
                        current_size = current_size // 2
                    else:
                        current_size = 0
            else:
                if not is_square:
                    if current_size % 2 == 0:
                        current_size = current_size // 2
                    else:
                        current_size = 0
                else:
                    current_size = 1
                    is_square = False
        
        if is_square:
            max_circles = 0
        else:
            if current_size % 2 == 0:
                max_circles = current_size // 2
            else:
                max_circles = 0
        
        print(max_circles)

if __name__ == '__main__':
    solve()