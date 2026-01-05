import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0

    N = int(input[idx].split()[0])
    idx += 1
    cities = input[idx].split()
    idx += 1

    M = int(input[idx].split()[0])
    idx += 1
    roads = {}
    for _ in range(M):
        parts = input[idx].split()
        c1, c2, d = parts[0], parts[1], int(parts[2])
        if c1 not in roads:
            roads[c1] = {}
        roads[c1][c2] = d
        idx += 1

    T = int(input[idx].split()[0])
    idx += 1
    for _ in range(T):
        parts = input[idx].split()
        K = int(parts[0])
        route = parts[1:]
        idx += 1

        if K == 1:
            print(0)
            continue

        if len(set(route)) != K:
            print("ERROR")
            continue

        valid = True
        for i in range(K - 1):
            if route[i] == route[i + 1]:
                valid = False
                break
            if route[i] not in roads or route[i + 1] not in roads[route[i]]:
                valid = False
                break

        if not valid:
            print("ERROR")
        else:
            total = 0
            for i in range(K - 1):
                total += roads[route[i]][route[i + 1]]
            print(total)

if __name__ == '__main__':
    solve()