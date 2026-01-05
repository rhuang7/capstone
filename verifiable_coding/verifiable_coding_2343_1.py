import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        d = int(data[index])
        m = int(data[index+1])
        index += 2
        if m == 1:
            results.append(0)
            continue
        # The number of valid arrays is equal to the sum of (2^k - 1) for k from 1 to log2(d)
        # Because for each bit position, we can choose to include or exclude it, but the sequence must be strictly increasing
        # So the total number of valid arrays is the sum of (2^k - 1) for k from 1 to log2(d)
        # But since d can be up to 1e9, we need to compute this efficiently
        # The sum is (2^(k+1) - 2) / 2 - k, which simplifies to 2^k - k - 1
        # But we need to compute it for all k such that 2^k <= d
        # So we find the maximum k such that 2^k <= d
        max_k = 0
        while (1 << (max_k + 1)) <= d:
            max_k += 1
        total = 0
        for k in range(1, max_k + 1):
            total += (1 << k) - k - 1
        results.append(total % m)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()