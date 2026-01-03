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
        # Check for any two equal subsequences
        # We can use the fact that if there is any character that appears at least twice,
        # then we can find two different subsequences of length 1 (the same character)
        # or longer if there are duplicates
        # So, check if any character appears at least twice
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        # If any character appears at least twice, then answer is yes
        # Because we can take two different positions of that character as two subsequences
        # For example, "aa" has "a" and "a" as two different subsequences
        # But if all characters are unique, then answer is no
        has_duplicate = any(count >= 2 for count in freq.values())
        print("yes" if has_duplicate else "no")

if __name__ == '__main__':
    solve()