import sys

def solve():
    q = int(sys.stdin.buffer.read().split())
    idx = 0
    for _ in range(q):
        s = sys.stdin.buffer.read().strip()
        t = sys.stdin.buffer.read().strip()
        idx += 2
        if s == t:
            print("YES")
            continue
        # Check if each character in s can be transformed to the corresponding character in t
        # using the allowed operations
        # The allowed operations allow us to propagate characters through the string
        # So, for each position i, s[i] can be changed to any character in s, and similarly for t
        # However, the key is that for each character in s and t, the multiset of characters must be the same
        # Because we can propagate characters through the string
        # So, we can check if the multiset of characters in s and t are the same
        # But wait, since we can change characters in s and t independently, the multiset of s and t must be the same
        # Because we can change s to any multiset of characters, and t to any multiset of characters
        # But the problem is to make s equal to t, so we need to check if s and t can be transformed into the same string
        # Which is possible if and only if the multiset of characters in s and t are the same
        # Because we can change s and t to any multiset of characters, but the final string must be the same
        # So, the multiset of characters in s and t must be the same
        # So, we can check if the sorted s and sorted t are the same
        if sorted(s) == sorted(t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()