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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        if n == 1:
            results.append("Yes")
            continue
        inc = []
        dec = []
        for i in range(n):
            if i == 0:
                inc.append(a[0])
                dec.append(a[0])
            else:
                if a[i] > a[i - 1]:
                    inc.append(a[i])
                    dec.append(a[i])
                elif a[i] < a[i - 1]:
                    dec.append(a[i])
                else:
                    inc.append(a[i])
                    dec.append(a[i])
        inc_max = max(inc)
        dec_min = min(dec)
        if inc_max > dec_min:
            results.append("Yes")
        else:
            results.append("No")
    print('\n'.join(results))