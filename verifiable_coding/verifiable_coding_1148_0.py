import sys

def is_better(a, b):
    for i in range(3):
        if a[i] < b[i]:
            return False
    return True

def can_order(a, b, c):
    # Check all permutations of the three people
    orderings = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
    for order in orderings:
        if is_better(order[0], order[1]) and is_better(order[1], order[2]):
            return True
    return False

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        a = list(map(int, input[idx:idx+3]))
        idx += 3
        b = list(map(int, input[idx:idx+3]))
        idx += 3
        c = list(map(int, input[idx:idx+3]))
        idx += 3
        if can_order(a, b, c):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()