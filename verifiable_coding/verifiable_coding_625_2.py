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
        prefix_mod = 0
        count = 0
        mod_count = {0: 1}
        for num in A:
            prefix_mod = (prefix_mod + num) % MOD
            if (prefix_mod) in mod_count:
                count += mod_count[prefix_mod]
            mod_count[prefix_mod] = mod_count.get(prefix_mod, 0) + 1
        print(count)

if __name__ == '__main__':
    solve()