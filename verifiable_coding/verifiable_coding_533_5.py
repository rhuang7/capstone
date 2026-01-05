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
        K = int(data[idx])
        N = int(data[idx+1])
        idx += 2
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        first = -1
        last = -1
        for i in range(N):
            if arr[i] == K:
                if first == -1:
                    first = i + 1  # 1-based index
                last = i + 1
        if first == -1:
            results.append("0")
        else:
            results.append(f"{first} {last}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()