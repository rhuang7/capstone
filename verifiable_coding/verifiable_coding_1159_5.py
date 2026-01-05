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
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                shanky = ch
                break
        for i in range(len(s)-1, -1, -1):
            if freq[s[i]] == 1:
                anku = s[i]
                break
        if shanky is not None and anku is not None:
            if shanky > anku:
                print("SHANKY")
            else:
                print("ANKU")
        elif shanky is not None:
            print("SHANKY")
        elif anku is not None:
            print("ANKU")
        else:
            print("PANDEY")

if __name__ == '__main__':
    solve()