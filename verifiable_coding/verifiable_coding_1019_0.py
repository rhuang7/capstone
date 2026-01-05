import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    S = int(data[idx])
    idx += 1
    results = []
    for _ in range(S):
        Ni = int(data[idx])
        idx += 1
        H = list(map(int, data[idx:idx+Ni]))
        idx += Ni
        if H[0] != 1 or H[-1] != 1:
            results.append("no")
            continue
        center = Ni // 2
        increasing = True
        for i in range(center):
            if H[i] != H[i-1] + 1:
                increasing = False
                break
        if not increasing:
            results.append("no")
            continue
        decreasing = True
        for i in range(center+1, Ni):
            if H[i] != H[i-1] - 1:
                decreasing = False
                break
        if decreasing:
            results.append("yes")
        else:
            results.append("no")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()