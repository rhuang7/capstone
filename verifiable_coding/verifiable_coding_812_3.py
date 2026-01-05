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
        n = int(data[idx])
        idx += 1
        D = list(map(int, data[idx:idx + n]))
        idx += n
        villagers = []
        dinosaurs = []
        for i in range(n):
            if D[i] > 0:
                villagers.append(i)
            else:
                dinosaurs.append(i)
        total = 0
        for v in villagers:
            for d in dinosaurs:
                total += abs(v - d)
        results.append(total // 2)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()