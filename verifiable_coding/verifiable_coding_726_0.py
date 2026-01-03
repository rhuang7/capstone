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
        counts = Counter()
        for _ in range(N):
            s = input[idx]
            idx += 1
            counts += Counter(s)
        # Calculate how many times each character in target can be used
        max_meals = 0
        for char, required in target.items():
            available = counts.get(char, 0)
            max_meals = min(max_meals, available // required)
        results.append(str(max_meals))

    print('\n'.join(results))