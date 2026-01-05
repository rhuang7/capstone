import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    arr = list(map(int, data[idx:idx+N]))
    idx += N
    Q = int(data[idx])
    idx += 1
    queries = []
    for _ in range(Q):
        T = data[idx]
        L = int(data[idx+1])
        R = int(data[idx+2])
        queries.append((T, L, R))
        idx += 3

    class SegmentTree:
        def __init__(self, data):
            self.n = len(data)
            self.size = 1
            while self.size < self.n:
                self.size <<= 1
            self.min_tree = [float('inf')] * (2 * self.size)
            self.max_tree = [-float('inf')] * (2 * self.size)
            self.second_min_tree = [float('inf')] * (2 * self.size)
            self.second_max_tree = [-float('inf')] * (2 * self.size)
            # Fill leaves
            for i in range(self.n):
                self.min_tree[self.size + i] = data[i]
                self.max_tree[self.size + i] = data[i]
                self.second_min_tree[self.size + i] = data[i]
                self.second_max_tree[self.size + i] = data[i]
            # Build the tree
            for i in range(self.size - 1, 0, -1):
                self.min_tree[i] = min(self.min_tree[2*i], self.min_tree[2*i+1])
                self.max_tree[i] = max(self.max_tree[2*i], self.max_tree[2*i+1])
                self.second_min_tree[i] = min(min(self.second_min_tree[2*i], self.second_min_tree[2*i+1]), self.min_tree[2*i], self.min_tree[2*i+1])
                self.second_max_tree[i] = max(max(self.second_max_tree[2*i], self.second_max_tree[2*i+1]), self.max_tree[2*i], self.max_tree[2*i+1])

        def update(self, pos, value):
            pos += self.size
            self.min_tree[pos] = value
            self.max_tree[pos] = value
            self.second_min_tree[pos] = value
            self.second_max_tree[pos] = value
            pos >>= 1
            while pos >= 1:
                left = 2 * pos
                right = 2 * pos + 1
                self.min_tree[pos] = min(self.min_tree[left], self.min_tree[right])
                self.max_tree[pos] = max(self.max_tree[left], self.max_tree[right])
                self.second_min_tree[pos] = min(min(self.second_min_tree[left], self.second_min_tree[right]), self.min_tree[left], self.min_tree[right])
                self.second_max_tree[pos] = max(max(self.second_max_tree[left], self.second_max_tree[right]), self.max_tree[left], self.max_tree[right])
                pos >>= 1

        def query_min(self, l, r):
            l += self.size
            r += self.size
            res = float('inf')
            while l <= r:
                if l % 2 == 1:
                    res = min(res, self.min_tree[l])
                    l += 1
                if r % 2 == 0:
                    res = min(res, self.min_tree[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def query_max(self, l, r):
            l += self.size
            r += self.size
            res = -float('inf')
            while l <= r:
                if l % 2 == 1:
                    res = max(res, self.max_tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, self.max_tree[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def query_second_min(self, l, r):
            l += self.size
            r += self.size
            res = float('inf')
            while l <= r:
                if l % 2 == 1:
                    res = min(res, self.second_min_tree[l])
                    l += 1
                if r % 2 == 0:
                    res = min(res, self.second_min_tree[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def query_second_max(self, l, r):
            l += self.size
            r += self.size
            res = -float('inf')
            while l <= r:
                if l % 2 == 1:
                    res = max(res, self.second_max_tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, self.second_max_tree[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def query_sum(self, l, r):
            l += self.size
            r += self.size
            res = 0
            while l <= r:
                if l % 2 == 1:
                    res += self.min_tree[l]
                    l += 1
                if r % 2 == 0:
                    res += self.min_tree[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

    st = SegmentTree(arr)

    for T, L, R in queries:
        if T == 'U':
            pos = L - 1
            value = R
            st.update(pos, value)
        elif T == 'A':
            res = st.query_sum(L-1, R-1)
            print(res)
        elif T == 'M':
            res = st.query_max(L-1, R-1)
            print(res)
        elif T == 'm':
            res = st.query_min(L-1, R-1)
            print(res)
        elif T == 'S':
            res = st.query_second_max(L-1, R-1)
            print(res)
        elif T == 's':
            res = st.query_second_min(L-1, R-1)
            print(res)
        else:
            print("!!!")