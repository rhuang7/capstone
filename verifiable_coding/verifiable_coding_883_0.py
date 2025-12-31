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
        for cnt in counts:
            if cnt < 0 or cnt > N - 1:
                results.append(-1)
                break
        else:
            total_pass = sum(counts) // N
            if total_pass < 0 or total_pass > N:
                results.append(-1)
            else:
                fail = 0
                for cnt in counts:
                    if cnt != total_pass - 1:
                        fail += 1
                results.append(fail)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()