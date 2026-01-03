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
        # The answer is the sum of (d - 2^k + 1) for all k such that 2^k <= d
        # This is because for each k, the number of valid arrays is (d - 2^k + 1)
        # and we sum over all k where 2^k <= d
        total = 0
        power = 1
        while power <= d:
            total += (d - power + 1)
            power <<= 1
        results.append(total % m)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()