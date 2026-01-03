import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    M = int(data[0])
    N = int(data[1])
    A = list(map(int, data[2:2+M]))
    
    total = M
    remaining_cuts = N
    
    for a in A:
        if remaining_cuts <= 0:
            break
        if a > remaining_cuts:
            total += remaining_cuts
            remaining_cuts = 0
        else:
            total += a
            remaining_cuts -= a
    
    print(total)

if __name__ == '__main__':
    solve()