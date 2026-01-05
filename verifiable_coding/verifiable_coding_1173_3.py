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
        prefix_xor = [0] * (N + 1)
        for i in range(N):
            prefix_xor[i + 1] = prefix_xor[i] ^ A[i]
        count = 0
        from collections import defaultdict
        freq = defaultdict(int)
        freq[0] = 1
        for j in range(N):
            for k in range(j + 1, N + 1):
                x = prefix_xor[k] ^ prefix_xor[j]
                if x in freq:
                    count += freq[x]
                freq[x] += 1
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()