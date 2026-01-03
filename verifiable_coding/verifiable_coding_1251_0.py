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

        if len(route) != K:
            print("ERROR")
            continue

        # Check if all cities in route exist
        for city in route:
            if city not in cities:
                print("ERROR")
                break
        else:
            # Check for consecutive duplicates
            for i in range(K - 1):
                if route[i] == route[i + 1]:
                    print("ERROR")
                    break
            else:
                # Check for first and last city being same
                if route[0] == route[-1]:
                    print("ERROR")
                    continue
                # Check for valid path
                total = 0
                current = route[0]
                valid = True
                for i in range(1, K):
                    if current not in roads or route[i] not in roads[current]:
                        valid = False
                        break
                    total += roads[current][route[i]]
                    current = route[i]
                if valid:
                    print(total)
                else:
                    print("ERROR")
            continue

if __name__ == '__main__':
    solve()