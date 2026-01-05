import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    S = data[idx]
    idx += 1
    Q = int(data[idx])
    idx += 1

    S = list(S)
    # For each query, we'll process it
    # We'll use a segment tree to handle range queries and point updates
    # Each node in the segment tree will store a bitmask of the characters present in the segment
    # For example, if a segment has 'a' and 'b', the bitmask will be 0b11 (binary) or 3 (decimal)
    # Since there are 26 lowercase letters, we need 26 bits

    # Build the segment tree
    size = 1
    while size < N:
        size <<= 1
    tree = [0] * (2 * size)
    # Fill the leaves
    for i in range(N):
        tree[size + i] = 1 << (ord(S[i]) - ord('a'))
    # Build the tree
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] | tree[2 * i + 1]

    def update(pos, value):
        # pos is 0-based
        pos += size
        tree[pos] = value
        pos >>= 1
        while pos >= 1:
            new_val = tree[2 * pos] | tree[2 * pos + 1]
            if tree[pos] == new_val:
                break
            tree[pos] = new_val
            pos >>= 1

    def query(l, r):
        # l and r are 0-based, inclusive
        l += size
        r += size
        res = 0
        while l <= r:
            if l % 2 == 1:
                res |= tree[l]
                l += 1
            if r % 2 == 0:
                res |= tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return bin(res).count('1')

    for _ in range(Q):
        if data[idx] == b'1':
            # Type 1: update
            i_q = int(data[idx + 1]) - 1
            c_q = data[idx + 2]
            idx += 3
            old_char = S[i_q]
            if old_char == c_q:
                continue
            S[i_q] = c_q
            update(i_q, 1 << (ord(c_q) - ord('a')))
        else:
            # Type 2: query
            l_q = int(data[idx + 1]) - 1
            r_q = int(data[idx + 2]) - 1
            idx += 3
            ans = query(l_q, r_q)
            print(ans)