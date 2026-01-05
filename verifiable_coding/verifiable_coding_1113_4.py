import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        A = list(map(int, input[idx:idx+N]))
        idx += N
        count = {}
        for num in A:
            count[num] = count.get(num, 0) + 1
        max_count = -1
        result_val = -1
        for key, val in count.items():
            if val > max_count or (val == max_count and key < result_val):
                max_count = val
                result_val = key
        print(f"{result_val} {max_count}")

if __name__ == '__main__':
    solve()