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
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for i, c in enumerate(s):
            if count[c] == 1:
                shanky = c
                break
        for i in range(len(s)-1, -1, -1):
            if count[s[i]] == 1:
                anku = s[i]
                break
        if shanky is not None and anku is not None:
            if shanky > anku:
                print("SHANKY")
            else:
                print("ANKU")
        else:
            print("PANDEY")

if __name__ == '__main__':
    solve()