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
        freq = {}
        for num in A:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        max_count = -1
        max_val = -1
        for key in freq:
            if freq[key] > max_count or (freq[key] == max_count and key < max_val):
                max_count = freq[key]
                max_val = key
        print(f"{max_val} {max_count}")

if __name__ == '__main__':
    solve()