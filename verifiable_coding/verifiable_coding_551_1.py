import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        n = len(s)
        if n < 2:
            print("no")
            continue
        freq = {}
        for i in range(n):
            if s[i] in freq:
                freq[s[i]].append(i)
            else:
                freq[s[i]] = [i]
        for char, indices in freq.items():
            if len(indices) >= 2:
                print("yes")
                break
        else:
            print("no")

if __name__ == '__main__':
    solve()