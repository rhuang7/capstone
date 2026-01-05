import sys

def solve():
    q = int(sys.stdin.buffer.read().split())
    idx = 0
    for _ in range(q):
        s = sys.stdin.buffer.read().strip().decode()
        t = sys.stdin.buffer.read().strip().decode()
        if s == t:
            print("YES")
            continue
        s_count = [0] * 26
        t_count = [0] * 26
        for c in s:
            s_count[ord(c) - ord('a')] += 1
        for c in t:
            t_count[ord(c) - ord('a')] += 1
        if s_count != t_count:
            print("NO")
            continue
        print("YES")

if __name__ == '__main__':
    solve()