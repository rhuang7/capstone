import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        chars = list(freq.keys())
        n = len(chars)
        if n < 3:
            print("Dynamic")
            continue
        
        # Generate all permutations of the characters
        from itertools import permutations
        found = False
        for perm in permutations(chars):
            f = [freq[c] for c in perm]
            valid = True
            for i in range(2, len(f)):
                if f[i] != f[i-1] + f[i-2]:
                    valid = False
                    break
            if valid:
                found = True
                break
        
        print("Dynamic" if found else "Not")

if __name__ == '__main__':
    solve()