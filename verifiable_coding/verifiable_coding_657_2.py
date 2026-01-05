import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    grid = []
    index = 2
    for _ in range(m):
        row = list(map(int, data[index:index+n]))
        grid.append(row)
        index += n

    max_score = 0

    for mask in range(1 << n):
        score = 0
        for i in range(m):
            row = grid[i]
            current = 0
            for j in range(n):
                if (mask >> j) & 1:
                    row[j] = 1 - row[j]
                current = current * 2 + row[j]
            score += current
        max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    solve()