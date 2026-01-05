import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def get_number(s):
        level = 1
        pos = 0
        for c in s:
            if c == 'l':
                pos = 2 * pos
            else:
                pos = 2 * pos + 1
            level += 1
        # Calculate the number based on level and position
        if level % 2 == 1:
            # Odd level: odd numbers
            return (level // 2) * 2 - 1 + pos
        else:
            # Even level: even numbers
            return (level // 2) * 2 + pos

    for s in cases:
        print(get_number(s) % MOD)

if __name__ == '__main__':
    solve()