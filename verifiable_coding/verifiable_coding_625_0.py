import sys

def solve():
    MOD = 10**9
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        A = list(map(int, input[idx:idx+N]))
        idx += N
        prefix_sum = 0
        count = 0
        freq = {0: 1}
        for num in A:
            prefix_sum += num
            rem = prefix_sum % MOD
            count += freq.get(rem, 0)
            freq[rem] = freq.get(rem, 0) + 1
        print(count)

if __name__ == '__main__':
    solve()