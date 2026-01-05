import sys
from itertools import permutations

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def count_valid_sequences(s):
        total = 0
        chars = list(s)
        n = len(chars)
        for perm in permutations(chars):
            seq = ''.join(perm)
            if 'kar' not in seq and 'shi' not in seq:
                total += 1
        return total

    for s in cases:
        print(count_valid_sequences(s))

if __name__ == '__main__':
    solve()