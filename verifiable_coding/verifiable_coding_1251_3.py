import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    ptr = 0

    N = int(input[ptr])
    ptr += 1
    cities = input[ptr].split()
    ptr += 1

    M = int(input[ptr])
    ptr += 1
    roads = {}
    for _ in range(M):
        parts = input[ptr].split()
        ptr += 1
        c1 = parts[0]
        c2 = parts[1]
        d = int(parts[2])
        if c1 not in roads:
            roads[c1] = {}
        roads[c1][c2] = d

    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        parts = input[ptr].split()
        ptr += 1
        K = int(parts[0])
        route = parts[1:]
        if K == 1:
            if route[0] in cities:
                print(0)
            else:
                print("ERROR")
            continue

        valid = True
        for i in range(K):
            if route[i] not in cities:
                valid = False
                break
        if not valid:
            print("ERROR")
            continue

        for i in range(K - 1):
            if route[i] == route[i + 1]:
                valid = False
                break
        if not valid:
            print("ERROR")
            continue

        for i in range(K - 1):
            if route[i + 1] not in roads.get(route[i], {}):
                valid = False
                break
        if not valid:
            print("ERROR")
            continue

        total = 0
        for i in range(K - 1):
            total += roads[route[i]][route[i + 1]]
        print(total)

if __name__ == '__main__':
    solve()