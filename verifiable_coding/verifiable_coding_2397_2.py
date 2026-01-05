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
        m = int(data[idx+1])
        idx += 2
        banned = set()
        for __ in range(n):
            s = data[idx]
            banned.add(s)
            idx += 1
        total = 1 << m
        k = total - n
        median_index = (k - 1) // 2
        found = False
        for i in range(total):
            s = bin(i)[2:].zfill(m)
            if s not in banned:
                if i == median_index:
                    results.append(s)
                found = True
                break
        if not found:
            results.append(bin(median_index)[2:].zfill(m))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()