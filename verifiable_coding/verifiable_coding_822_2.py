import sys
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    while True:
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        dna_sequences = []
        for _ in range(n):
            if idx >= len(data):
                break
            seq = data[idx].strip()
            idx += 1
            if not seq:
                continue
            dna_sequences.append(seq)
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