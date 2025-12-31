import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        a = []
        b = []
        i = 0
        j = 0
        while len(a) < n and len(b) < n:
            if i < len(p) and j < len(p):
                if p[i] < p[j]:
                    a.append(p[i])
                    i += 1
                else:
                    b.append(p[j])
                    j += 1
            else:
                break
        if len(a) != n or len(b) != n:
            results.append("NO")
            continue
        valid = True
        used = set()
        for num in p:
            if num in used:
                valid = False
                break
            used.add(num)
        if not valid:
            results.append("NO")
            continue
        results.append("YES")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()