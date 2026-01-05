import sys
import math

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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        freq = {}
        for num in a:
            temp = num
            for p in range(2, int(math.isqrt(temp)) + 1):
                if temp % p == 0:
                    count = 0
                    while temp % p == 0:
                        temp //= p
                        count += 1
                    if count >= 2:
                        freq[p] = 1
                        break
            if temp > 1:
                freq[temp] = 1
        for p in freq:
            results.append(str(p))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()