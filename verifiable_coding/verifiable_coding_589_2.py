import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for P in cases:
        max_jump = 1
        days = 0
        i = 0
        while i < len(P):
            if P[i] == '#':
                i += 1
            else:
                # Need to find the next '#'
                j = i + 1
                while j < len(P) and P[j] == '.':
                    j += 1
                if j >= len(P):
                    break
                required = j - i
                if required > max_jump:
                    days += 1
                    max_jump = required
                i = j + 1
        print(days)

if __name__ == '__main__':
    solve()