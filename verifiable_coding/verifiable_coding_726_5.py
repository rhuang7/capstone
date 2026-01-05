import sys

def solve():
    from collections import Counter

    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []

    target = Counter("codechef")
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        count = Counter()
        for _ in range(N):
            s = input[idx]
            idx += 1
            count += Counter(s)
        max_meals = 0
        for char, required in target.items():
            max_meals = min(max_meals, count.get(char, 0) // required)
        results.append(str(max_meals))

    print('\n'.join(results))