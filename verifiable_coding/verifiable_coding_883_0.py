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
        idx += 1
        counts = list(map(int, data[idx:idx+N]))
        idx += N
        total_pass = 0
        for count in counts:
            if count < 0 or count > N - 1:
                results.append(-1)
                break
        else:
            total_pass = 0
            for count in counts:
                total_pass += count
            total_pass = total_pass // N
            if total_pass < 0 or total_pass > N:
                results.append(-1)
            else:
                fail = N - total_pass
                possible = True
                for count in counts:
                    if count != total_pass - 1 and count != total_pass:
                        possible = False
                        break
                if possible:
                    results.append(fail)
                else:
                    results.append(-1)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()