import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def is_w_string(s):
        if s.count('#') != 3:
            return 0
        p = [i for i, c in enumerate(s) if c == '#']
        if len(p) != 3:
            return 0
        p1, p2, p3 = p
        if p2 - p1 <= 1 or p3 - p2 <= 1:
            return 0
        # Check if there are any '#' between p1 and p2 or between p2 and p3
        if any(s[i] == '#' for i in range(p1+1, p2)):
            return 0
        if any(s[i] == '#' for i in range(p2+1, p3)):
            return 0
        # Check if each segment has only one character
        def check_segment(s, a, b):
            if a >= b:
                return False
            c = s[a]
            for i in range(a, b+1):
                if s[i] != c:
                    return False
            return True
        if not check_segment(s, 0, p1-1):
            return 0
        if not check_segment(s, p1+1, p2-1):
            return 0
        if not check_segment(s, p2+1, p3-1):
            return 0
        if not check_segment(s, p3+1, len(s)-1):
            return 0
        return len(s)

    max_len = 0
    for s in cases:
        max_len = max(max_len, is_w_string(s))
    print(max_len)

if __name__ == '__main__':
    solve()