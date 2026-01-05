import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    queries = data[1:T+1]

    def min_grid_area(s):
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

    def try_insert(s, char):
        for i in range(len(s) + 1):
            new_s = s[:i] + char + s[i:]
            area = min_grid_area(new_s)
            if area < min_grid_area(s):
                return area
        return min_grid_area(s)

    for s in queries:
        original_area = min_grid_area(s)
        min_area = original_area
        for c in ['W', 'A', 'S', 'D']:
            area = try_insert(s, c)
            if area < min_area:
                min_area = area
        print(min_area)

if __name__ == '__main__':
    solve()