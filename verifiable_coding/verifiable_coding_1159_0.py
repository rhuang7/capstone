import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    for s in cases:
        shanky = None
        anku = None
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for i, c in enumerate(s):
            if freq[c] == 1:
                shanky = c
                break
        for i in range(len(s)-1, -1, -1):
            if freq[s[i]] == 1:
                anku = s[i]
                break
        if shanky is None or anku is None:
            print("PANDEY")
        else:
            if shanky > anku:
                print("SHANKY")
            else:
                print("ANKU")

if __name__ == '__main__':
    solve()