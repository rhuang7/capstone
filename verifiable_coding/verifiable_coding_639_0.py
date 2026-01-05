import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def is_dynamic(s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        chars = list(freq.keys())
        n = len(chars)
        if n < 3:
            return True
        # Generate all permutations of chars
        from itertools import permutations
        for perm in permutations(chars):
            # Check if the condition holds for all i >= 3
            valid = True
            for i in range(2, len(perm)):
                if freq[perm[i]] != freq[perm[i-1]] + freq[perm[i-2]]:
                    valid = False
                    break
            if valid:
                return True
        return False

    for s in cases:
        if is_dynamic(s):
            print("Dynamic")
        else:
            print("Not")

if __name__ == '__main__':
    solve()