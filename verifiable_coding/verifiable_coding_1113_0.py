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
        max_element = -1

        for num, cnt in count.items():
            if cnt > max_count or (cnt == max_count and num < max_element):
                max_count = cnt
                max_element = num

        print(f"{max_element} {max_count}")

if __name__ == '__main__':
    solve()