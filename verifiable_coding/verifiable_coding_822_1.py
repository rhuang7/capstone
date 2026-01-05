import sys
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    while True:
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        if n == 0 and m == 0:
            break
        dna_sequences = data[idx:idx+n]
        idx += n
        count = defaultdict(int)
        for seq in dna_sequences:
            count[seq] += 1
        res = [0] * (n + 1)
        for v in count.values():
            res[v] += 1
        for i in range(1, n + 1):
            print(res[i])

if __name__ == '__main__':
    solve()