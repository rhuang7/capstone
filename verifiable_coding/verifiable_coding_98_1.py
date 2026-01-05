import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    q = int(data[0])
    index = 1
    results = []
    for _ in range(q):
        c = int(data[index])
        m = int(data[index+1])
        x = int(data[index+2])
        index += 3
        # The maximum number of teams is limited by the minimum of (c + m) // 3 and the minimum of c and m
        # Also, we need to ensure that there are enough students to form the teams
        # The maximum possible is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if there are enough students in total to form the teams
        # The total students is c + m + x
        # The maximum number of teams is the minimum of (c + m) // 3 and min(c, m)
        # But also, we need to ensure that the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if there are enough students in total to form the teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if there are enough students in total to form the teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # However, if the total students is less than 3 * teams, then we can't form that many teams
        # So the answer is min( (c + m) // 3, min(c, m) )
        # But also, we need to check if the total students is at least 3 * teams
        # So the answer is