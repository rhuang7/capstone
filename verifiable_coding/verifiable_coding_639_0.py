import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def is_dynamic(s):
        from collections import Counter
        freq = Counter(s)
        chars = list(freq.keys())
        if len(chars) < 3:
            return True
        n = len(chars)
        for perm in range(1 << n):
            # Generate permutation
            perm_chars = []
            for i in range(n):
                if perm & (1 << i):
                    perm_chars.append(chars[i])
            # Check condition
            f = [freq[c] for c in perm_chars]
            valid = True
            for i in range(2, n):
                if f[i] != f[i-1] + f[i-2]:
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