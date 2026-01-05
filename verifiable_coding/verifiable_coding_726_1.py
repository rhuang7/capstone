import sys

def solve():
    import sys
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
        meals = 0
        for char, needed in target.items():
            meals += count[char] // needed
        results.append(str(meals))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()