import sys

def is_better(x, y):
    for i in range(3):
        if x[i] < y[i]:
            return False
    return True

def can_order(team):
    a, b, c = team[0], team[1], team[2]
    # Check all permutations of the three members
    for perm in [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]:
        if is_better(perm[0], perm[1]) and is_better(perm[1], perm[2]):
            return True
    return False

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        a = list(map(int, input[idx:idx+3]))
        idx += 3
        b = list(map(int, input[idx:idx+3]))
        idx += 3
        c = list(map(int, input[idx:idx+3]))
        idx += 3
        team = [a, b, c]
        if can_order(team):
            results.append("yes")
        else:
            results.append("no")
    print("\n".join(results))

if __name__ == '__main__':
    solve()