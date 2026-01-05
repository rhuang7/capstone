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
                    cnt = 0
                    while temp % p == 0:
                        temp //= p
                        cnt += 1
                    if cnt >= 2:
                        freq[p] = freq.get(p, 0) + 1
            if temp > 1:
                freq[temp] = freq.get(temp, 0) + 1
        for p in freq:
            if freq[p] >= 2:
                results.append(p)
                break
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()