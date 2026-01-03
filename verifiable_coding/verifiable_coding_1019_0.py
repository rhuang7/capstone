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
        if Ni % 2 == 0:
            results.append("no")
            continue
        valid = True
        for i in range(center):
            if H[i] != H[i-1] + 1:
                valid = False
                break
        if not valid:
            results.append("no")
            continue
        for i in range(center+1, Ni):
            if H[i] != H[i-1] - 1:
                valid = False
                break
        if valid:
            results.append("yes")
        else:
            results.append("no")
    print("\n".join(results))