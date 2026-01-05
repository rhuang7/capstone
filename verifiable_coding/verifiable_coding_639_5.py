import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def is_dynamic(s):
        if len(set(s)) < 3:
            return True
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        freq_list = list(freq.values())
        freq_list.sort()
        if len(freq_list) == 3:
            a, b, c = freq_list
            return a == b + c
        else:
            from itertools import permutations
            for perm in permutations(freq_list):
                if perm[0] == perm[1] + perm[2] and perm[1] == perm[2] + perm[3]:
                    return True
            return False

    for s in cases:
        if is_dynamic(s):
            print("Dynamic")
        else:
            print("Not")

if __name__ == '__main__':
    solve()