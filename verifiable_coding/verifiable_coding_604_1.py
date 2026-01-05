import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        idx += 2
        grid = []
        for _ in range(R):
            row = list(map(int, data[idx:idx+C]))
            grid.append(row)
            idx += C
        is_stable = True
        for i in range(R):
            for j in range(C):
                count = 0
                if i > 0:
                    count += 1
                if i < R - 1:
                    count += 1
                if j > 0:
                    count += 1
                if j < C - 1:
                    count += 1
                if count <= grid[i][j]:
                    is_stable = False
                    break
            if not is_stable:
                break
        results.append("Stable" if is_stable else "Unstable")
    print('\n'.join(results))