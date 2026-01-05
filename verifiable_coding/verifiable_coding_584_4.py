import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    strings = input[1:N+1]
    
    for s in strings:
        if not s:
            print(0)
            continue
        i = 0
        square_size = 0
        circle_diameter = 0
        can_inscribe = True
        while i < len(s):
            if s[i] == '1':
                if square_size == 0:
                    square_size = 1
                else:
                    if square_size % 2 == 0:
                        can_inscribe = False
                        break
                    square_size = square_size // 2
            else:
                if circle_diameter == 0:
                    circle_diameter = 1
                else:
                    if circle_diameter % 2 == 0:
                        can_inscribe = False
                        break
                    circle_diameter = circle_diameter // 2
            i += 1
        if can_inscribe and square_size > 0 and circle_diameter > 0:
            print(circle_diameter // 2)
        else:
            print(0)

if __name__ == '__main__':
    solve()