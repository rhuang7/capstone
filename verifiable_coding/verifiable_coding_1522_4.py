import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def is_w_string(s):
        if '#' not in s:
            return 0
        p1 = s.index('#')
        if p1 == len(s) - 1 or p1 == 0:
            return 0
        p2 = s.find('#', p1 + 1)
        if p2 == -1 or p2 == len(s) - 1:
            return 0
        p3 = s.find('#', p2 + 1)
        if p3 == -1:
            return 0
        # Check if there are exactly 3 '#'
        if s.count('#') != 3:
            return 0
        # Check if there are no '#' between p1 and p2, p2 and p3
        if s[p1+1:p2].count('#') > 0 or s[p2+1:p3].count('#') > 0:
            return 0
        # Check if each segment has same characters
        seg1 = s[0:p1]
        seg2 = s[p1+1:p2]
        seg3 = s[p2+1:p3]
        seg4 = s[p3+1:]
        if len(seg1) == 0 or len(seg2) == 0 or len(seg3) == 0 or len(seg4) == 0:
            return 0
        if seg1.count(seg1[0]) != len(seg1):
            return 0
        if seg2.count(seg2[0]) != len(seg2):
            return 0
        if seg3.count(seg3[0]) != len(seg3):
            return 0
        if seg4.count(seg4[0]) != len(seg4):
            return 0
        return len(s)
    
    max_len = 0
    for s in cases:
        max_len = max(max_len, is_w_string(s))
    print(max_len)

if __name__ == '__main__':
    solve()