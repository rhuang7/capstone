import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for p in cases:
        max_jump = 1
        days = 0
        i = 0
        while i < len(p):
            if p[i] == '#':
                i += 1
            else:
                # Need to jump over the '.'s
                j = i + 1
                while j < len(p) and p[j] == '.':
                    j += 1
                if j == len(p):
                    # End of passage
                    break
                required_jump = j - i
                if required_jump > max_jump:
                    days += 1
                    max_jump = required_jump
                i = j
        print(days)

if __name__ == '__main__':
    solve()