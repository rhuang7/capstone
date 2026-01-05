import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def is_w_string(s):
        if s.count('#') != 3:
            return 0
        p = [i for i, c in enumerate(s) if c == '#']
        if len(p) != 3:
            return 0
        p1, p2, p3 = p
        if p2 - p1 - 1 > 0 or p3 - p2 - 1 > 0:
            return 0
        # Check if the segments between the # have the same character
        # Segment 0: from start to p1-1
        # Segment 1: from p1+1 to p2-1
        # Segment 2: from p2+1 to p3-1
        # Segment 3: from p3+1 to end
        # Each segment must have the same character
        # Also, each segment must be non-empty
        segs = []
        if p1 > 0:
            segs.append(s[0:p1])
        if p2 > p1 + 1:
            segs.append(s[p1+1:p2])
        if p3 > p2 + 1:
            segs.append(s[p2+1:p3])
        if p3 < len(s)-1:
            segs.append(s[p3+1:])
        # Check if all segments have the same character
        if not segs:
            return 0
        first_char = segs[0][0]
        for seg in segs:
            if seg and seg[0] != first_char:
                return 0
        # All segments have the same character
        return len(segs[0]) + len(segs[1]) + len(segs[2]) + len(segs[3]) + 3

    max_len = 0
    for s in cases:
        max_len = max(max_len, is_w_string(s))
    print(max_len)

if __name__ == '__main__':
    solve()