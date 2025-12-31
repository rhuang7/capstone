import sys

def solve():
    import sys
    from collections import Counter

    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1

    for _ in range(T):
        N = int(input[idx])
        idx += 1
        A = list(map(int, input[idx:idx+N]))
        idx += N

        count = Counter(A)
        max_count = -1
        max_value = -1

        for key, val in count.items():
            if val > max_count or (val == max_count and key < max_value):
                max_count = val
                max_value = key

        print(f"{max_value} {max_count}")

if __name__ == '__main__':
    solve()