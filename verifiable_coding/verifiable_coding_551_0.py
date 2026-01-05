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
        # Check if there are at least two identical characters
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        # If any character appears at least twice, then there are two equal subsequences
        # For example, if a character appears twice, then the two single characters are equal subsequences
        if any(count >= 2 for count in freq.values()):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()