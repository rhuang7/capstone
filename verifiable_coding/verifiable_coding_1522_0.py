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
        # Check if the parts between the '#' are all the same character
        def get_part(s, a, b):
            if a > b:
                return ''
            return s[a:b+1]
        part1 = get_part(s, 0, p1-1)
        part2 = get_part(s, p1+1, p2-1)
        part3 = get_part(s, p2+1, p3-1)
        part4 = get_part(s, p3+1, len(s)-1)
        if len(part1) > 0 and len(part2) > 0 and len(part3) > 0 and len(part4) > 0:
            if part1[0] != part2[0] or part2[0] != part3[0] or part3[0] != part4[0]:
                return 0
        elif len(part1) > 0 and len(part2) > 0 and len(part3) > 0:
            if part1[0] != part2[0] or part2[0] != part3[0]:
                return 0
        elif len(part1) > 0 and len(part2) > 0 and len(part4) > 0:
            if part1[0] != part2[0] or part2[0] != part4[0]:
                return 0
        elif len(part1) > 0 and len(part3) > 0 and len(part4) > 0:
            if part1[0] != part3[0] or part3[0] != part4[0]:
                return 0
        elif len(part1) > 0 and len(part2) > 0:
            if part1[0] != part2[0]:
                return 0
        elif len(part2) > 0 and len(part3) > 0:
            if part2[0] != part3[0]:
                return 0
        elif len(part3) > 0 and len(part4) > 0:
            if part3[0] != part4[0]:
                return 0
        elif len(part1) > 0:
            return 1
        elif len(part2) > 0:
            return 1
        elif len(part3) > 0:
            return 1
        elif len(part4) > 0:
            return 1
        else:
            return 0
        return len(s)
    
    max_len = 0
    for s in cases:
        max_len = max(max_len, is_w_string(s))
    print(max_len)

if __name__ == '__main__':
    solve()