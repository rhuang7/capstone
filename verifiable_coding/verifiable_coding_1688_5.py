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
        n = int(data[idx])
        idx += 1
        lis = list(map(int, data[idx:idx+n]))
        idx += n
        res = []
        prev = 0
        for i in range(n):
            if i == 0:
                res.append(str(9 - lis[0] + 1))
                prev = lis[0]
            else:
                if lis[i] == lis[i-1]:
                    res.append(str(9 - lis[i] + 1))
                else:
                    if lis[i] > lis[i-1]:
                        res.append(str(9 - lis[i] + 1))
                    else:
                        res.append(str(9 - lis[i] + 1))
        results.append(''.join(res))
    print('\n'.join(results))