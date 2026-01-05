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
        N = int(data[idx])
        P = int(data[idx+1])
        idx += 2
        solves = list(map(int, data[idx:idx+N]))
        idx += N
        cakewalk = 0
        hard = 0
        for s in solves:
            if s >= P // 2:
                cakewalk += 1
            elif s <= P // 10:
                hard += 1
        if cakewalk == 1 and hard == 2:
            results.append("yes")
        else:
            results.append("no")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()