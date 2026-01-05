import sys
from collections import Counter

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        cnt = Counter(s)
        freq = list(cnt.values())
        n = len(s)
        freq.sort()
        m = len(freq)
        total = 0
        for i in range(m):
            if i == 0:
                total += freq[i]
            else:
                total += freq[i] - freq[i-1]
        print(total)

if __name__ == '__main__':
    solve()