import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def get_number(s):
        level = 1
        node = 1
        for c in s:
            if c == 'l':
                node = 2 * node
            else:
                node = 2 * node + 1
            level += 1
        return node

    for s in cases:
        print(get_number(s))

if __name__ == '__main__':
    solve()