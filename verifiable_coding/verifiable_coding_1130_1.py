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
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        ages = list(map(int, data[idx:idx+N]))
        idx += N
        risk = [a for a in ages if a <= 9 or a >= 80]
        non_risk = [a for a in ages if 10 <= a <= 79]
        days_risk = (len(risk) + D - 1) // D
        days_non_risk = (len(non_risk) + D - 1) // D
        results.append(days_risk + days_non_risk)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()