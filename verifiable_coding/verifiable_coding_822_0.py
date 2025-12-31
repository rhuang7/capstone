import sys
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    while True:
        line = data[idx].strip()
        while line == '':
            idx += 1
            line = data[idx].strip()
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        idx += 1
        dna_sequences = []
        for _ in range(n):
            while True:
                line = data[idx].strip()
                if line != '':
                    break
                idx += 1
            dna_sequences.append(line)
            idx += 1
        count = defaultdict(int)
        for seq in dna_sequences:
            count[seq] += 1
        res = [0] * (n + 1)
        for v in count.values():
            res[v] += 1
        for i in range(1, n + 1):
            print(res[i])
        idx += 1

if __name__ == '__main__':
    solve()