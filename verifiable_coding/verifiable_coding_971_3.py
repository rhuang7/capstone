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
        if len(set(A)) == 1:
            results.append(0)
            continue
        freq = {}
        for num in A:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        min_moves = N - max_freq
        results.append(min_moves)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()