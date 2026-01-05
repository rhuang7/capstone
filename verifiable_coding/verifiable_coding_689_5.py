import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    a = []
    b = []
    idx = 1
    for _ in range(t):
        a.append(int(data[idx]))
        b.append(int(data[idx+1]))
        idx += 2
    positions = set(a)
    for i in range(t):
        target = a[i] + b[i]
        if target in positions:
            for j in range(t):
                if a[j] == target and b[j] == -b[i]:
                    print("YES")
                    return
    print("NO")

if __name__ == '__main__':
    solve()