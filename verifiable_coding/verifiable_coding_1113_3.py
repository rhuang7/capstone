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
        max_val = -1

        for key, val in count.items():
            if val > max_count or (val == max_count and key < max_val):
                max_count = val
                max_val = key

        print(f"{max_val} {max_count}")

if __name__ == '__main__':
    solve()