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
        C1 = parts[0]
        C2 = parts[1]
        D = int(parts[2])
        if C1 not in roads:
            roads[C1] = {}
        roads[C1][C2] = D
        idx += 1

    T = int(input[idx].split()[0])
    idx += 1
    for _ in range(T):
        parts = input[idx].split()
        K = int(parts[0])
        route = parts[1:]
        idx += 1

        # Check if all cities in route exist
        valid = True
        for city in route:
            if city not in cities:
                valid = False
                break

        if not valid:
            print("ERROR")
            continue

        # Check if consecutive cities are different
        for i in range(K - 1):
            if route[i] == route[i + 1]:
                valid = False
                break

        if not valid:
            print("ERROR")
            continue

        # Check if any city is visited more than once
        visited = set()
        for city in route:
            if city in visited:
                valid = False
                break
            visited.add(city)

        if not valid:
            print("ERROR")
            continue

        # Calculate total distance
        total = 0
        for i in range(K - 1):
            C1 = route[i]
            C2 = route[i + 1]
            if C1 not in roads or C2 not in roads[C1]:
                valid = False
                break
            total += roads[C1][C2]

        if not valid:
            print("ERROR")
        else:
            print(total)

if __name__ == '__main__':
    solve()