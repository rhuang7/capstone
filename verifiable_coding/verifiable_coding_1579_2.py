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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        seen = set()
        for i in range(N):
            curr_or = 0
            for j in range(i, N):
                curr_or |= A[j]
                if curr_or in seen:
                    results.append("NO")
                    break
                seen.add(curr_or)
            else:
                continue
            break
        else:
            results.append("YES")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()