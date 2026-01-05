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
        # The allowed operations allow us to propagate characters to the left or right
        # So, for each position i, the character in s[i] must be the same as t[i] or can be transformed
        # to t[i] by propagating from left or right
        # However, the operation allows us to set either character to the other, so we can propagate
        # any character to any position as long as it's present in the string
        # So, the key is that for each character in t, it must be present in s and vice versa
        # But since we can perform operations on both strings, we need to check if the multiset of characters
        # in s and t are the same
        if sorted(s) != sorted(t):
            print("NO")
        else:
            print("YES")

if __name__ == '__main__':
    solve()