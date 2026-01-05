import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    S = int(input[idx])
    idx += 1
    for _ in range(S):
        Ni = int(input[idx])
        idx += 1
        H = list(map(int, input[idx:idx+Ni]))
        idx += Ni
        if H[0] != 1 or H[-1] != 1:
            print("no")
            continue
        center = Ni // 2
        valid = True
        for i in range(center):
            if H[i] != H[i-1] + 1:
                valid = False
                break
        for i in range(center+1, Ni):
            if H[i] != H[i-1] - 1:
                valid = False
                break
        if valid:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()