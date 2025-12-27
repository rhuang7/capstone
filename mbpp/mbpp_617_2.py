def check(candidate):
    assert candidate(3,4,11)==3.5
    assert candidate(3,4,0)==0
    assert candidate(11,14,11)==1


def jumps_to_reach_d0(start, jump_length):
    x, y = start
    jumps = 0
    while x != d or y != 0:
        if y > 0:
            y -= jump_length
            jumps += 1
        elif y < 0:
            y += jump_length
            jumps += 1
        else:
            break
    return jumps

check(jumps_to_reach_d0)