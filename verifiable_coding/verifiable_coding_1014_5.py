import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    from collections import defaultdict

    def is_power_of_two(n):
        return (n & (n - 1)) == 0

    def get_powers_of_two_up_to_max_length(max_len):
        powers = []
        power = 1
        while True:
            s = str(power)
            if len(s) > max_len:
                break
            powers.append(power)
            power *= 2
        return powers

    for s in cases:
        n = len(s)
        max_len = n
        powers = get_powers_of_two_up_to_max_length(max_len)
        valid_numbers = set()
        for num in powers:
            s_num = str(num)
            if len(s_num) > n:
                continue
            if len(s_num) < n:
                continue
            if sorted(s_num) == sorted(s):
                valid_numbers.add(num)
        if not valid_numbers:
            print(-1)
        else:
            total = sum(valid_numbers) % MOD
            print(total)

if __name__ == '__main__':
    solve()