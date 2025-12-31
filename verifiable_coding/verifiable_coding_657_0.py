import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    grid = []
    idx = 2
    for _ in range(m):
        row = list(map(int, data[idx:idx+n]))
        grid.append(row)
        idx += n

    max_score = 0

    for mask in range(1 << n):
        score = 0
        for i in range(m):
            row = grid[i]
            toggled = []
            for j in range(n):
                if (mask >> j) & 1:
                    toggled.append(1 - row[j])
                else:
                    toggled.append(row[j])
            num = 0
            for bit in toggled:
                num = (num << 1) | bit
            score += num
        max_score = max(max_score, score)

    print(max_score)

if __name__ == '__main__':
    solve()