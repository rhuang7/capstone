import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    strings = input[1:N+1]

    for s in strings:
        max_circles = 0
        current_size = 0
        is_square = True
        for c in s:
            if c == '1':
                if not is_square:
                    break
                current_size += 1
            else:
                if is_square:
                    if current_size % 2 == 0:
                        max_circles += current_size // 2
                    else:
                        max_circles = 0
                    is_square = False
                else:
                    if current_size % 2 == 0:
                        max_circles += current_size // 2
                    else:
                        max_circles = 0
        print(max_circles)

if __name__ == '__main__':
    solve()