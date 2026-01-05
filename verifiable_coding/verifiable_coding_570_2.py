import sys
import math
from itertools import permutations

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    forbidden = {"kar", "shi"}

    def count_valid_sequences(s):
        total = math.factorial(len(s))
        invalid = 0
        for perm in permutations(s):
            perm_str = ''.join(perm)
            if 'kar' in perm_str or 'shi' in perm_str:
                invalid += 1
        return total - invalid

    for s in cases:
        print(count_valid_sequences(s))

if __name__ == '__main__':
    solve()