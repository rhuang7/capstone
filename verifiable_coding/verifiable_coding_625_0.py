import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    MOD = 10**9
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
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