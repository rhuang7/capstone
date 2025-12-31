import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    s_list = data[1:T+1]

    def compute_grid(s):
        x = 0
        y = 0
        max_x = 0
        min_x = 0
        max_y = 0
        min_y = 0
        for c in s:
            if c == 'W':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'A':
                x -= 1
            elif c == 'D':
                x += 1
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        return width * height

    for s in s_list:
        original_area = compute_grid(s)
        min_area = original_area
        for c in ['W', 'A', 'S', 'D']:
            for i in range(len(s) + 1):
                new_s = s[:i] + c + s[i:]
                area = compute_grid(new_s)
                if area < min_area:
                    min_area = area
        print(min_area)

if __name__ == '__main__':
    solve()