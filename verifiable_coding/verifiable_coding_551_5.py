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
        # Check if there are at least two equal characters
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        # If any character appears at least twice, then there are two equal subsequences
        # Because we can take two different positions of the same character
        if any(v >= 2 for v in freq.values()):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()