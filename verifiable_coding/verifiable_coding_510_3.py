import sys

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
    from collections import defaultdict

    # For each position, track the character
    # For each query of type 2, we need to find the number of unique characters in a range
    # We can use a segment tree with each node storing a bitmask of the characters present in the range
    # Each character is represented by a bit (a=0, b=1, ..., z=25)
    # For a segment tree, each node will store a bitmask of the characters in its range

    # Build the segment tree
    class SegmentTree:
        def __init__(self, data):
            self.n = len(data)
            self.size = 1
            while self.size < self.n:
                self.size <<= 1
            self.tree = [0] * (2 * self.size)
            # Fill the leaves
            for i in range(self.n):
                self.tree[self.size + i] = 1 << (ord(data[i]) - ord('a'))
            # Build the tree
            for i in range(self.size - 1, 0, -1):
                self.tree[i] = self.tree[2 * i] | self.tree[2 * i + 1]

        def update(self, pos, value):
            pos += self.size
            self.tree[pos] = value
            pos >>= 1
            while pos >= 1:
                new_val = self.tree[2 * pos] | self.tree[2 * pos + 1]
                if self.tree[pos] == new_val:
                    break
                self.tree[pos] = new_val
                pos >>= 1

        def query(self, l, r):
            # [l, r) interval
            l += self.size
            r += self.size
            res = 0
            while l < r:
                if l % 2 == 1:
                    res |= self.tree[l]
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    res |= self.tree[r]
                l >>= 1
                r >>= 1
            return res

    st = SegmentTree(S)

    for _ in range(Q):
        query_type = int(data[idx])
        idx += 1
        if query_type == 1:
            i_q = int(data[idx]) - 1
            idx += 1
            c_q = data[idx]
            idx += 1
            if S[i_q] != c_q:
                S[i_q] = c_q
                bit = 1 << (ord(c_q) - ord('a'))
                st.update(i_q, bit)
        else:
            l_q = int(data[idx]) - 1
            idx += 1
            r_q = int(data[idx]) - 1
            idx += 1
            mask = st.query(l_q, r_q + 1)
            count = bin(mask).count('1')
            print(count)

if __name__ == '__main__':
    solve()