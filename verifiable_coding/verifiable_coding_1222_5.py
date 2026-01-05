import sys
from collections import Counter

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    strings = input[1:T+1]

    for s in strings:
        n = len(s)
        count = 0
        freq = Counter()
        for i in range(n):
            freq[s[i]] += 1
            for j in range(i+1, n):
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    count += 1
        print(count)

if __name__ == '__main__':
    solve()