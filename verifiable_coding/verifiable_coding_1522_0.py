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
        # Check if the substrings between the '#' have the same character
        left1 = s[0:p1]
        left2 = s[p1+1:p2]
        left3 = s[p2+1:p3]
        left4 = s[p3+1:]
        if len(left1) > 0 and len(left2) > 0 and len(left3) > 0 and len(left4) > 0:
            if left1[0] != left2[0] or left2[0] != left3[0] or left3[0] != left4[0]:
                return 0
        elif len(left1) > 0 and len(left2) > 0 and len(left3) > 0:
            if left1[0] != left2[0] or left2[0] != left3[0]:
                return 0
        elif len(left1) > 0 and len(left2) > 0 and len(left4) > 0:
            if left1[0] != left2[0] or left2[0] != left4[0]:
                return 0
        elif len(left1) > 0 and len(left3) > 0 and len(left4) > 0:
            if left1[0] != left3[0] or left3[0] != left4[0]:
                return 0
        elif len(left2) > 0 and len(left3) > 0 and len(left4) > 0:
            if left2[0] != left3[0] or left3[0] != left4[0]:
                return 0
        elif len(left1) > 0 and len(left2) > 0:
            if left1[0] != left2[0]:
                return 0
        elif len(left2) > 0 and len(left3) > 0:
            if left2[0] != left3[0]:
                return 0
        elif len(left3) > 0 and len(left4) > 0:
            if left3[0] != left4[0]:
                return 0
        # Check if all substrings have the same character
        if len(left1) > 0 and len(left2) > 0 and len(left3) > 0 and len(left4) > 0:
            if left1[0] != left2[0] or left2[0] != left3[0] or left3[0] != left4[0]:
                return 0
        elif len(left1) > 0 and len(left2) > 0 and len(left3) > 0:
            if left1[0] != left2[0] or left2[0] != left3[0]:
                return 0
        elif len(left1) > 0 and len(left2) > 0 and len(left4) > 0:
            if left1[0] != left2[0] or left2[0] != left4[0]:
                return 0
        elif len(left1) > 0 and len(left3) > 0 and len(left4) > 0:
            if left1[0] != left3[0] or left3[0] != left4[0]:
                return 0
        elif len(left2) > 0 and len(left3) > 0 and len(left4) > 0:
            if left2[0] != left3[0] or left3[0] != left4[0]:
                return 0
        elif len(left1) > 0 and len(left2) > 0:
            if left1[0] != left2[0]:
                return 0
        elif len(left2) > 0 and len(left3) > 0:
            if left2[0] != left3[0]:
                return 0
        elif len(left3) > 0 and len(left4) > 0:
            if left3[0] != left4[0]:
                return 0
        # Calculate the length of the W string
        return len(s)
    
    max_len = 0
    for s in cases:
        if is_w_string(s) > max_len:
            max_len = is_w_string(s)
    print(max_len)

if __name__ == '__main__':
    solve()