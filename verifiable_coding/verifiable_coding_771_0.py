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
        M = int(data[idx])
        F = int(data[idx+1])
        idx += 2
        S = list(map(int, data[idx:idx+N]))
        idx += N
        multan_wins = 0
        fultan_wins = 0
        for s in S:
            if s % M == 0:
                multan_wins += 1
            if s % F == 0:
                fultan_wins += 1
        total_wins = multan_wins + fultan_wins
        accuracy = (total_wins / N) * 100
        if accuracy >= 70:
            results.append("Yes")
            if multan_wins > fultan_wins:
                results.append("Multan")
            elif multan_wins < fultan_wins:
                results.append("Fultan")
            else:
                results.append("Both")
        else:
            results.append("No")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()