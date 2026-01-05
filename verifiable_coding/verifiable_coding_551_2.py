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
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        # If any character appears at least twice, then there are two equal subsequences
        # Because we can take two different positions of the same character
        # For example, if 'a' appears at positions i and j, then the subsequences "a" and "a" are equal
        # and they are different sequences
        has_duplicate = any(count >= 2 for count in freq.values())
        print("yes" if has_duplicate else "no")

if __name__ == '__main__':
    solve()