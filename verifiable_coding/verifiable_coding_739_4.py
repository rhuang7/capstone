import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        path = input[idx:]
        idx += len(path)
        distance = 0
        dir = 'N'
        x, y = 0, 0
        for part in path:
            if part.isdigit():
                distance += int(part)
            else:
                if dir == 'N':
                    if part == 'R':
                        dir = 'E'
                    else:
                        dir = 'W'
                elif dir == 'E':
                    if part == 'R':
                        dir = 'S'
                    else:
                        dir = 'N'
                elif dir == 'S':
                    if part == 'R':
                        dir = 'W'
                    else:
                        dir = 'E'
                elif dir == 'W':
                    if part == 'R':
                        dir = 'N'
                    else:
                        dir = 'S'
        if distance == 0:
            print("0.0N")
        else:
            print(f"{distance}.0{dir}")

if __name__ == '__main__':
    solve()