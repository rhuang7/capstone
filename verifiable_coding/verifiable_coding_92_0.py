import sys

def solve():
    q = int(sys.stdin.buffer.readline())
    for _ in range(q):
        s = sys.stdin.buffer.readline().strip()
        t = sys.stdin.buffer.readline().strip()
        if s == t:
            print("YES")
            continue
        # Check if each character in s can be transformed to the corresponding character in t
        # using the allowed operations
        # The allowed operations allow us to spread a character to adjacent positions
        # So, for each position i, the character in s[i] can be transformed to any character in the same connected component
        # So, for the transformation to be possible, the multiset of characters in s and t must be the same
        # But since we can perform operations on both strings, we need to check if s and t have the same multiset of characters
        # However, the operation allows us to spread characters, so we can transform s into t if the multiset of characters in s and t are the same
        # But since we can also transform t into s, the multiset of s and t must be the same
        # So, check if the multiset of s and t are the same
        from collections import Counter
        if Counter(s) == Counter(t):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()